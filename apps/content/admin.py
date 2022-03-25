from apps.content.models import WhyToWorkWithUsPage, Service, SubmitReferralPage, StaffCategory, \
    ApplicantsHowItWorksPage, WorkingInAustriaPage, VideoResumePage
from django.contrib import admin
from solo.admin import SingletonModelAdmin


admin.site.register(Service)
admin.site.register(StaffCategory)

admin.site.register(SubmitReferralPage, SingletonModelAdmin)
admin.site.register(WhyToWorkWithUsPage, SingletonModelAdmin)
admin.site.register(ApplicantsHowItWorksPage, SingletonModelAdmin)
admin.site.register(WorkingInAustriaPage, SingletonModelAdmin)
admin.site.register(VideoResumePage, SingletonModelAdmin)
