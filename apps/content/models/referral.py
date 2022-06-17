from django.utils.translation import gettext_lazy as _
from django.db import models


class Referral(models.Model):
    completed = models.BooleanField(default=False, blank=True)
    your_name = models.CharField(_('Your Name'), max_length=200)
    your_email = models.CharField(_('Your E-Mail'), max_length=200)
    referral_name = models.CharField(_('Referral Name'), max_length=200)
    referral_email = models.CharField(_('Referral E-Mail'), max_length=200)
    referral_phone = models.CharField(_('Referral Phone'), max_length=200)
    referral_job = models.CharField(_('Referral Job'), max_length=50)
    referral_resume = models.FileField(_('Referral Resume'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Referral'
        verbose_name_plural = 'Referrals'

    def __str__(self):
        if self.completed:
            return 'Completed: {}'.format(self.referral_name)
        return '{}'.format(self.referral_name)
