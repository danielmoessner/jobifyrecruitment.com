from solo.models import SingletonModel
from django.db import models
from tinymce import models as tinymce_models


###
# other
###
class Service(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()
    ordering = models.IntegerField(0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['ordering']


class StaffCategory(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    ordering = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Staff Category'
        verbose_name_plural = 'Staff Categories'
        ordering = ['ordering']


###
# pages
###
class WhyToWorkWithUsPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=100)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200)
    text_left = tinymce_models.HTMLField(verbose_name='Text > Left')
    text_right = tinymce_models.HTMLField(verbose_name='Text > Right')
    text_button = models.CharField(verbose_name='Text > Button', max_length=200)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Why To Work With Us'


class SubmitReferralPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=100)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200)
    text_left = tinymce_models.HTMLField(verbose_name='Text > Left')
    text_right = tinymce_models.HTMLField(verbose_name='Text > Right')
    text_button = models.CharField(verbose_name='Text > Button', max_length=200)
    #
    faq_title = models.CharField(verbose_name='FAQ > Title', max_length=100)
    faq_question_1 = models.CharField(verbose_name='FAQ > Question 1', max_length=100, blank=True)
    faq_answer_1 = models.TextField(verbose_name='FAQ > Answer 1', blank=True)
    faq_question_2 = models.CharField(verbose_name='FAQ > Question 2', max_length=100, blank=True)
    faq_answer_2 = models.TextField(verbose_name='FAQ > Answer 2', blank=True)
    faq_question_3 = models.CharField(verbose_name='FAQ > Question 3', max_length=100, blank=True)
    faq_answer_3 = models.TextField(verbose_name='FAQ > Answer 3', blank=True)
    faq_question_4 = models.CharField(verbose_name='FAQ > Question 4', max_length=100, blank=True)
    faq_answer_4 = models.TextField(verbose_name='FAQ > Answer 4', blank=True)
    faq_question_5 = models.CharField(verbose_name='FAQ > Question 5', max_length=100, blank=True)
    faq_answer_5 = models.TextField(verbose_name='FAQ > Answer 5', blank=True)
    faq_question_6 = models.CharField(verbose_name='FAQ > Question 6', max_length=100, blank=True)
    faq_answer_6 = models.TextField(verbose_name='FAQ > Answer 6', blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Submit A Referral Page'


class ApplicantsHowItWorksPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=100)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text')
    text_button = models.CharField(verbose_name='Text > Button', max_length=200)
    #
    plan_title = models.CharField(verbose_name='Plan > Title', max_length=100)
    plan_1 = models.TextField(verbose_name='Plan > Step 1', blank=True)
    plan_2 = models.TextField(verbose_name='Plan > Step 2', blank=True)
    plan_3 = models.TextField(verbose_name='Plan > Step 3', blank=True)
    plan_4 = models.TextField(verbose_name='Plan > Step 4', blank=True)
    plan_button = models.CharField(verbose_name='Plan > Button', max_length=100)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Applicants How It Works'


class ServicesPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=100)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text')

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Courses'


class WorkingInAustriaPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=100)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text')

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Working In Austria'


class VideoResumePage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=100)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text')
    #
    benefits_left_title = models.CharField(verbose_name='Benefits > Title Left', max_length=200)
    benefits_left_text = models.TextField(verbose_name='Benefits > Text Left')
    benefits_right_title = models.CharField(verbose_name='Benefits > Title Right', max_length=200)
    benefits_right_text = models.TextField(verbose_name='Benefits > Text Right')
    #
    video_title = models.CharField(verbose_name='Video > Title', max_length=200)
    #
    faq_title = models.CharField(verbose_name='FAQ > Title', max_length=100)
    faq_question_1 = models.CharField(verbose_name='FAQ > Question 1', max_length=100, blank=True)
    faq_answer_1 = models.TextField(verbose_name='FAQ > Answer 1', blank=True)
    faq_question_2 = models.CharField(verbose_name='FAQ > Question 2', max_length=100, blank=True)
    faq_answer_2 = models.TextField(verbose_name='FAQ > Answer 2', blank=True)
    faq_question_3 = models.CharField(verbose_name='FAQ > Question 3', max_length=100, blank=True)
    faq_answer_3 = models.TextField(verbose_name='FAQ > Answer 3', blank=True)
    faq_question_4 = models.CharField(verbose_name='FAQ > Question 4', max_length=100, blank=True)
    faq_answer_4 = models.TextField(verbose_name='FAQ > Answer 4', blank=True)
    faq_question_5 = models.CharField(verbose_name='FAQ > Question 5', max_length=100, blank=True)
    faq_answer_5 = models.TextField(verbose_name='FAQ > Answer 5', blank=True)
    faq_question_6 = models.CharField(verbose_name='FAQ > Question 6', max_length=100, blank=True)
    faq_answer_6 = models.TextField(verbose_name='FAQ > Answer 6', blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Video Resume'
