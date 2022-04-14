from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from apps.content.models import WhyToWorkWithUsPage, Service, SubmitReferralPage, StaffCategory, \
    ApplicantsHowItWorksPage, WorkingInAustriaPage, VideoResumePage, EmployerFaqPage, StaffingSolutionsPage, \
    SubmitPositionPage, ServicesPage, AboutPage, Applicant, Company, Referral, User, Member, MemberCategory, PortalPage, \
    ContactPage
from django.contrib import admin
from solo.admin import SingletonModelAdmin


class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name",)}),
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


# unregister
admin.site.unregister(Site)
admin.site.unregister(Group)
# register
admin.site.register(Member)
admin.site.register(MemberCategory)
admin.site.register(User, UserAdmin)
admin.site.register(Referral)
admin.site.register(Company)
admin.site.register(Applicant)
admin.site.register(Service)
admin.site.register(StaffCategory)
# register pages
admin.site.register(PortalPage, SingletonModelAdmin)
admin.site.register(SubmitReferralPage, SingletonModelAdmin)
admin.site.register(WhyToWorkWithUsPage, SingletonModelAdmin)
admin.site.register(ApplicantsHowItWorksPage, SingletonModelAdmin)
admin.site.register(WorkingInAustriaPage, SingletonModelAdmin)
admin.site.register(VideoResumePage, SingletonModelAdmin)
admin.site.register(EmployerFaqPage, SingletonModelAdmin)
admin.site.register(StaffingSolutionsPage, SingletonModelAdmin)
admin.site.register(SubmitPositionPage, SingletonModelAdmin)
admin.site.register(ServicesPage, SingletonModelAdmin)
admin.site.register(AboutPage, SingletonModelAdmin)
admin.site.register(ContactPage, SingletonModelAdmin)
