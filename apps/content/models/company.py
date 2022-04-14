from apps.content.models import StaffCategory
from django.db import models


class Company(models.Model):
    # choices
    JOB_DURATION_CHOICES = (
        ('4', '4 Months'),
        ('6', '6 Months'),
        ('8', '8 Months'),
        ('12', '12 Months'),
        ('PERMANENT', 'Permanent'),
    )
    #
    manager_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=30)
    looking_for = models.ForeignKey(StaffCategory, on_delete=models.SET_NULL, null=True)
    job_position = models.CharField(max_length=200)
    job_duration = models.CharField(choices=JOB_DURATION_CHOICES, max_length=100)
    job_start = models.DateField()
    job_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return '{}'.format(self.company_name)
