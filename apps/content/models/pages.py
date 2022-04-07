from solo.models import SingletonModel
from django.db import models
from tinymce import models as tinymce_models


class WhyToWorkWithUsPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    text_button = models.CharField(verbose_name='Text > Button', max_length=200, blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Why To Work With Us'


class SubmitReferralPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    text_button = models.CharField(verbose_name='Text > Button', max_length=200, blank=True)
    #
    faq_title = models.CharField(verbose_name='FAQ > Title', max_length=1000)
    faq_question_1 = models.CharField(verbose_name='FAQ > Question 1', max_length=1000, blank=True)
    faq_answer_1 = models.TextField(verbose_name='FAQ > Answer 1', blank=True)
    faq_question_2 = models.CharField(verbose_name='FAQ > Question 2', max_length=1000, blank=True)
    faq_answer_2 = models.TextField(verbose_name='FAQ > Answer 2', blank=True)
    faq_question_3 = models.CharField(verbose_name='FAQ > Question 3', max_length=1000, blank=True)
    faq_answer_3 = models.TextField(verbose_name='FAQ > Answer 3', blank=True)
    faq_question_4 = models.CharField(verbose_name='FAQ > Question 4', max_length=1000, blank=True)
    faq_answer_4 = models.TextField(verbose_name='FAQ > Answer 4', blank=True)
    faq_question_5 = models.CharField(verbose_name='FAQ > Question 5', max_length=1000, blank=True)
    faq_answer_5 = models.TextField(verbose_name='FAQ > Answer 5', blank=True)
    faq_question_6 = models.CharField(verbose_name='FAQ > Question 6', max_length=1000, blank=True)
    faq_answer_6 = models.TextField(verbose_name='FAQ > Answer 6', blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Submit A Referral'


class SubmitReferralThanksPage(SingletonModel):
    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Submit A Referral Thanks'


class ApplicantsHowItWorksPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    text_button = models.CharField(verbose_name='Text > Button', max_length=200, blank=True)
    #
    plan_title = models.CharField(verbose_name='Plan > Title', max_length=1000, blank=True)
    plan_1 = models.TextField(verbose_name='Plan > Step 1', blank=True)
    plan_2 = models.TextField(verbose_name='Plan > Step 2', blank=True)
    plan_3 = models.TextField(verbose_name='Plan > Step 3', blank=True)
    plan_4 = models.TextField(verbose_name='Plan > Step 4', blank=True)
    plan_button = models.CharField(verbose_name='Plan > Button', max_length=1000, blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Applicants How It Works'


class ServicesPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Courses'


class WorkingInAustriaPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Working In Austria'


class VideoResumePage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    #
    benefits_left_title = models.CharField(verbose_name='Benefits > Title Left', max_length=200, blank=True)
    benefits_left_text = models.TextField(verbose_name='Benefits > Text Left', blank=True)
    benefits_right_title = models.CharField(verbose_name='Benefits > Title Right', max_length=200, blank=True)
    benefits_right_text = models.TextField(verbose_name='Benefits > Text Right', blank=True)
    #
    video_title = models.CharField(verbose_name='Video > Title', max_length=200, blank=True)
    #
    faq_title = models.CharField(verbose_name='FAQ > Title', max_length=1000, blank=True)
    faq_question_1 = models.CharField(verbose_name='FAQ > Question 1', max_length=1000, blank=True)
    faq_answer_1 = models.TextField(verbose_name='FAQ > Answer 1', blank=True)
    faq_question_2 = models.CharField(verbose_name='FAQ > Question 2', max_length=1000, blank=True)
    faq_answer_2 = models.TextField(verbose_name='FAQ > Answer 2', blank=True)
    faq_question_3 = models.CharField(verbose_name='FAQ > Question 3', max_length=1000, blank=True)
    faq_answer_3 = models.TextField(verbose_name='FAQ > Answer 3', blank=True)
    faq_question_4 = models.CharField(verbose_name='FAQ > Question 4', max_length=1000, blank=True)
    faq_answer_4 = models.TextField(verbose_name='FAQ > Answer 4', blank=True)
    faq_question_5 = models.CharField(verbose_name='FAQ > Question 5', max_length=1000, blank=True)
    faq_answer_5 = models.TextField(verbose_name='FAQ > Answer 5', blank=True)
    faq_question_6 = models.CharField(verbose_name='FAQ > Question 6', max_length=1000, blank=True)
    faq_answer_6 = models.TextField(verbose_name='FAQ > Answer 6', blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Video Resume'


class EmployerFaqPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    #
    faq_question_1 = models.CharField(verbose_name='FAQ > Question 1', max_length=1000, blank=True)
    faq_answer_1 = models.TextField(verbose_name='FAQ > Answer 1', blank=True)
    faq_question_2 = models.CharField(verbose_name='FAQ > Question 2', max_length=1000, blank=True)
    faq_answer_2 = models.TextField(verbose_name='FAQ > Answer 2', blank=True)
    faq_question_3 = models.CharField(verbose_name='FAQ > Question 3', max_length=1000, blank=True)
    faq_answer_3 = models.TextField(verbose_name='FAQ > Answer 3', blank=True)
    faq_question_4 = models.CharField(verbose_name='FAQ > Question 4', max_length=1000, blank=True)
    faq_answer_4 = models.TextField(verbose_name='FAQ > Answer 4', blank=True)
    faq_question_5 = models.CharField(verbose_name='FAQ > Question 5', max_length=1000, blank=True)
    faq_answer_5 = models.TextField(verbose_name='FAQ > Answer 5', blank=True)
    faq_question_6 = models.CharField(verbose_name='FAQ > Question 6', max_length=1000, blank=True)
    faq_answer_6 = models.TextField(verbose_name='FAQ > Answer 6', blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Employer FAQ'


class StaffingSolutionsPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=1000, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=1000, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    #
    solutions_title = models.CharField(verbose_name='Solutions > Title', max_length=1000, blank=True)
    #
    cta_title = models.CharField(verbose_name='Cta > Title', max_length=1000, blank=True)
    cta_text = models.TextField(verbose_name='Cta > Text', blank=True)
    cta_button = models.CharField(verbose_name='Cta > Button', max_length=1000, blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Staffing Solutions'


class SubmitPositionPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    form_title = models.CharField(verbose_name='Form > Title', max_length=1000, blank=True)
    form_text = tinymce_models.HTMLField(verbose_name='Form > Text', blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Submit A Position'


class SubmitPositionThanksPage(SingletonModel):
    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Submit A Position Thanks'


class InitiativeApplicationThanksPage(SingletonModel):
    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Initiative Application Thanks'


class AboutPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > About'


class PortalPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=1000, blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Portal'
