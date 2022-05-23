from django.contrib.admin.utils import flatten_fieldsets
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin, TabbedDjangoJqueryTranslationAdmin
from modeltranslation.utils import unique

from apps.content.models import WhyToWorkWithUsPage, Service, SubmitReferralPage, StaffCategory, \
    ApplicantsHowItWorksPage, WorkingInAustriaPage, VideoResumePage, EmployerFaqPage, StaffingSolutionsPage, \
    SubmitPositionPage, ServicesPage, AboutPage, Applicant, Company, Referral, User, Member, MemberCategory, \
    PortalPage, ContactPage, ImprintPage, ContactThanksPage, SubmitReferralThanksPage, SubmitPositionThanksPage, \
    InitiativeApplicationThanksPage, IndexPage, InitiativeApplicationPage, JobSeekerFaqPage, Navigation, AgbPage, \
    PrivacyPage, EmployerHowItWorksPage, Footer
from django.contrib import admin
from solo.admin import SingletonModelAdmin


class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Information", {"fields": ("name",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "name")
    list_filter = ("groups",)
    search_fields = ("email", "name")
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


class GroupedTranslationAdmin(TranslationAdmin):
    group_fieldsets = True


class PageAdmin(SingletonModelAdmin, TranslationAdmin):
    group_fieldsets = True

    def _group_fieldsets(self, fieldsets):
        # Fieldsets are not grouped by default. The function is activated by
        # setting TranslationAdmin.group_fieldsets to True. If the admin class
        # already defines a fieldset, we leave it alone and assume the author
        # has done whatever grouping for translated fields they desire.
        if self.group_fieldsets is True:
            flattened_fieldsets = flatten_fieldsets(fieldsets)

            # Create a fieldset to group each translated field's localized fields
            fields = sorted((f for f in self.opts.get_fields() if f.concrete))
            untranslated_fields = [
                f
                for f in fields
                if (
                    # Exclude the primary key field
                        f is not self.opts.auto_field
                        # Exclude non-editable fields
                        and f.editable
                        # Exclude the translation fields
                        and not hasattr(f, 'translated_field')
                        # Honour field arguments. We rely on the fact that the
                        # passed fieldsets argument is already fully filtered
                        # and takes options like exclude into account.
                        and f.name in flattened_fieldsets
                )
            ]
            fieldsets = []

            temp_fieldsets = {}
            for orig_field, trans_fields in self.trans_opts.fields.items():
                trans_fieldnames = [f.name for f in sorted(trans_fields, key=lambda x: x.name)]
                if any(f in trans_fieldnames for f in flattened_fieldsets):
                    # Extract the original field's verbose_name for use as this
                    # fieldset's label - using gettext_lazy in your model
                    # declaration can make that translatable.
                    label = self.model._meta.get_field(orig_field).verbose_name.capitalize()
                    temp_fieldsets[orig_field] = (
                        label,
                        {'fields': trans_fieldnames, 'classes': ('mt-fieldset collapse',)},
                    )

            fields_order = unique(
                f.translated_field.name
                for f in self.opts.fields
                if hasattr(f, 'translated_field') and f.name in flattened_fieldsets
            )
            for field_name in fields_order:
                fieldsets.append(temp_fieldsets.pop(field_name))

            for field in untranslated_fields:
                fieldsets.append((
                    field.verbose_name,
                    {'fields': [field.name], 'classes': ('mt-fieldset collapse',)},
                ))

            assert not temp_fieldsets  # cleaned

        return fieldsets


# unregister
admin.site.unregister(Site)
admin.site.unregister(Group)
# register
admin.site.register(Member, GroupedTranslationAdmin)
admin.site.register(MemberCategory, GroupedTranslationAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Referral)
admin.site.register(Company)
admin.site.register(Applicant)
admin.site.register(Service, GroupedTranslationAdmin)
admin.site.register(StaffCategory, GroupedTranslationAdmin)
admin.site.register(Navigation, PageAdmin)
admin.site.register(Footer, PageAdmin)
# register pages
admin.site.register(PortalPage, PageAdmin)
admin.site.register(SubmitReferralPage, PageAdmin)
admin.site.register(WhyToWorkWithUsPage, PageAdmin)
admin.site.register(ApplicantsHowItWorksPage, PageAdmin)
admin.site.register(EmployerHowItWorksPage, PageAdmin)
admin.site.register(WorkingInAustriaPage, PageAdmin)
admin.site.register(VideoResumePage, PageAdmin)
admin.site.register(EmployerFaqPage, PageAdmin)
admin.site.register(StaffingSolutionsPage, PageAdmin)
admin.site.register(SubmitPositionPage, PageAdmin)
admin.site.register(ServicesPage, PageAdmin)
admin.site.register(AboutPage, PageAdmin)
admin.site.register(ContactPage, PageAdmin)
admin.site.register(ImprintPage, PageAdmin)
admin.site.register(ContactThanksPage, PageAdmin)
admin.site.register(SubmitReferralThanksPage, PageAdmin)
admin.site.register(SubmitPositionThanksPage, PageAdmin)
admin.site.register(InitiativeApplicationPage, PageAdmin)
admin.site.register(InitiativeApplicationThanksPage, PageAdmin)
admin.site.register(IndexPage, PageAdmin)
admin.site.register(JobSeekerFaqPage, PageAdmin)
admin.site.register(AgbPage, PageAdmin)
admin.site.register(PrivacyPage, PageAdmin)
