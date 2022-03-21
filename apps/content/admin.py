from apps.content.models import WhyToWorkWithUsPage, Service
from django.contrib import admin
from solo.admin import SingletonModelAdmin


admin.site.register(WhyToWorkWithUsPage, SingletonModelAdmin)
admin.site.register(Service)
