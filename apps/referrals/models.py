from django.db import models


class Referral(models.Model):
    your_name = models.CharField(max_length=200)
    your_email = models.CharField(max_length=200)
    referral_name = models.CharField(max_length=200)
    referral_email = models.CharField(max_length=200)
    referral_phone = models.CharField(max_length=200)
    referral_job = models.CharField(max_length=50)
    referral_resume = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Referral'
        verbose_name_plural = 'Referrals'

    def __str__(self):
        return '{}'.format(self.referral_name)
