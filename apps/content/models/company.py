from django.db import models


class Company(models.Model):
    manager_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=30)
    looking_for = models.CharField(max_length=200)
    job_position = models.CharField(max_length=200)
    job_duration = models.CharField(max_length=1000)
    job_start = models.DateField()
    job_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return '{}'.format(self.company_name)
