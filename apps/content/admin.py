from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from modeltranslation.admin import TranslationAdmin
from apps.content.models import WhyToWorkWithUsPage, Service, SubmitReferralPage, StaffCategory, \
    ApplicantsHowItWorksPage, WorkingInAustriaPage, VideoResumePage, EmployerFaqPage, StaffingSolutionsPage, \
    SubmitPositionPage, ServicesPage, AboutPage, Applicant, Company, Referral, User, Member, MemberCategory, \
    PortalPage, ContactPage, ImprintPage, ContactThanksPage, SubmitReferralThanksPage, SubmitPositionThanksPage, \
    InitiativeApplicationThanksPage, IndexPage, InitiativeApplicationPage, JobSeekerFaqPage, Navigation
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
# register pages
admin.site.register(PortalPage, PageAdmin)
admin.site.register(SubmitReferralPage, PageAdmin)
admin.site.register(WhyToWorkWithUsPage, PageAdmin)
admin.site.register(ApplicantsHowItWorksPage, PageAdmin)
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
