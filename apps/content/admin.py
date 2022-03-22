from apps.content.models import WhyToWorkWithUsPage, Service, SubmitReferralPage, StaffCategory
from django.contrib import admin
from solo.admin import SingletonModelAdmin


admin.site.register(SubmitReferralPage, SingletonModelAdmin)
admin.site.register(WhyToWorkWithUsPage, SingletonModelAdmin)
admin.site.register(Service)
admin.site.register(StaffCategory)