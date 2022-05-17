from django.utils.translation import gettext_lazy as _
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
    YES_NO_CHOICES = (
        ('Y', _('Yes')),
        ('N', _('No')),
    )
    #
    manager_name = models.CharField(_('Manager Name'), max_length=200)
    company_name = models.CharField(_('Company Name'), max_length=200)
    company_email = models.EmailField(_('Company E-Mail'))
    company_phone = models.CharField(_('Company Phone'), max_length=30, blank=True)
    looking_for = models.ForeignKey(StaffCategory, verbose_name=_('Looking for'), on_delete=models.SET_NULL, null=True)
    job_position = models.CharField(_('Job Position'), max_length=200)
    job_duration = models.CharField(_('Job Duration'), choices=JOB_DURATION_CHOICES, max_length=100)
    job_start = models.DateField(_('Job Start'))
    job_description = models.TextField(_('Job Description'))
    accommodation = models.CharField(_('Accomodation provided'), choices=YES_NO_CHOICES, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return '{}'.format(self.company_name)
