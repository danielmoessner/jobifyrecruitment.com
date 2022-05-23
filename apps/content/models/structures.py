from solo.models import SingletonModel
from django.db import models


class Navigation(SingletonModel):
    #
    job_seeker = models.CharField(verbose_name='Job Seeker', blank=True, max_length=200)
    job_seeker_column_1 = models.CharField(verbose_name='Job Seeker > Column 1', blank=True, max_length=200)
    job_seeker_why_work_with_us = models.CharField(verbose_name='Job Seeker > Why Work With Us', blank=True,
                                                   max_length=200)
    job_seeker_submit_a_referral = models.CharField(verbose_name='Job Seeker > Submit A Referral', blank=True,
                                                    max_length=200)
    job_seeker_how_it_works = models.CharField(verbose_name='Job Seeker > How It Works', blank=True, max_length=200)
    job_seeker_column_2 = models.CharField(verbose_name='Job Seeker > Column 2', blank=True, max_length=200)
    job_seeker_service_1 = models.ForeignKey('Service', verbose_name='Job Seeker > Service 1', blank=True, null=True,
                                             on_delete=models.SET_NULL, related_name='navigation_1')
    job_seeker_service_2 = models.ForeignKey('Service', verbose_name='Job Seeker > Service 2', blank=True, null=True,
                                             on_delete=models.SET_NULL, related_name='navigation_2')
    job_seeker_service_3 = models.ForeignKey('Service', verbose_name='Job Seeker > Service 3', blank=True, null=True,
                                             on_delete=models.SET_NULL, related_name='navigation_3')
    job_seeker_service_4 = models.ForeignKey('Service', verbose_name='Job Seeker > Service 4', blank=True, null=True,
                                             on_delete=models.SET_NULL, related_name='navigation_4')
    job_seeker_column_3 = models.CharField(verbose_name='Job Seeker > Column 3', blank=True, max_length=200)
    job_seeker_working_in_austria = models.CharField(verbose_name='Job Seeker > Working In Austria', blank=True,
                                                     max_length=200)
    job_seeker_faqs = models.CharField(verbose_name='Job Seeker > FAQs', blank=True, max_length=200)
    job_seeker_video_resume = models.CharField(verbose_name='Job Seeker > Video Resume', blank=True, max_length=200)
    #
    employer = models.CharField(verbose_name='Employer', blank=True, max_length=200)
    employer_column_1 = models.CharField(verbose_name='Employer > Column 1', blank=True, max_length=200)

    employer_column_2 = models.CharField(verbose_name='Employer > Column 2', blank=True, max_length=200)
    employer_submit_a_position = models.CharField(verbose_name='Employer > Submit A Position', blank=True,
                                                  max_length=200)
    employer_how_it_works = models.CharField(verbose_name='Employer > How It Works', blank=True, max_length=200)
    employer_column_3 = models.CharField(verbose_name='Employer > Column 3', blank=True, max_length=200)
    employer_video_resume = models.CharField(verbose_name='Employer > Video Resume', blank=True, max_length=200)
    employer_faqs = models.CharField(verbose_name='Employer > FAQs', blank=True, max_length=200)
    #
    about = models.CharField(verbose_name='About', blank=True, max_length=200)
    #
    contact = models.CharField(verbose_name='Contact', blank=True, max_length=200)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Navigation'


class Footer(SingletonModel):
    column_1_text = models.TextField('Column 1 > Text', blank=True)
    column_1_phone = models.CharField('Column 1 > Phone', blank=True, max_length=1000)
    column_1_mail = models.CharField('Column 1 > Mail', blank=True, max_length=1000)

    column_2_title = models.CharField('Column 2 > Title', blank=True, max_length=1000)
    column_2_text_1 = models.CharField('Column 2 > Text 1', blank=True, max_length=1000)
    column_2_text_2 = models.CharField('Column 2 > Text 2', blank=True, max_length=1000)
    column_2_text_3 = models.CharField('Column 2 > Text 3', blank=True, max_length=1000)

    column_3_title = models.CharField('Column 3 > Title', blank=True, max_length=1000)
    column_3_text_1 = models.CharField('Column 3 > Text 1', blank=True, max_length=1000)
    column_3_text_2 = models.CharField('Column 3 > Text 2', blank=True, max_length=1000)
    column_3_text_3 = models.CharField('Column 3 > Text 3', blank=True, max_length=1000)

    column_4_title = models.CharField('Column 4 > Title', blank=True, max_length=1000)
    column_4_text_1 = models.CharField('Column 4 > Text 1', blank=True, max_length=1000)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Footer'
