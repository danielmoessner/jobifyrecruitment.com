from solo.models import SingletonModel
from django.db import models
from tinymce import models as tinymce_models

SIZE_CHOICES = (
    ('SMALL', 'Small'),
    ('NORMAL', 'Normal'),
    ('LARGE', 'Large'),
)


class BasePage(SingletonModel):
    meta_title = models.TextField(verbose_name='Meta > Title', blank=True)
    meta_description = models.TextField(verbose_name='Meta > Description', blank=True)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        abstract = True


class IndexPage(BasePage):
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    header_text = models.TextField(verbose_name='Header > Text', blank=True)
    header_button_left = models.CharField(verbose_name='Header > Button Left', max_length=100, blank=True)
    header_button_right = models.CharField(verbose_name='Header > Button Right', max_length=100, blank=True)
    #
    services_left = models.CharField(verbose_name='Services > Left', max_length=300, blank=True)
    services_button_left = models.CharField(verbose_name='Services > Button Left', max_length=100, blank=True)
    services_center = models.CharField(verbose_name='Services > Center', max_length=300, blank=True)
    services_button_center = models.CharField(verbose_name='Services > Button Center', max_length=100, blank=True)
    services_right = models.CharField(verbose_name='Services > Right', max_length=300, blank=True)
    services_button_right = models.CharField(verbose_name='Services > Button Right', max_length=100, blank=True)
    #
    text_title = models.TextField(verbose_name='Text > Title', max_length=1000, blank=True)
    text_text = models.TextField(verbose_name='Text > Text', blank=True)
    #
    applicants_title = models.CharField(verbose_name='Applicants > Title', max_length=1000, blank=True)
    applicants_text = models.TextField(verbose_name='Applicants > Text', blank=True)
    applicants_button = models.CharField(verbose_name='Applicants > Button', max_length=200, blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=500, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > Home'


class WhyToWorkWithUsPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.TextField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    text_button = models.CharField(verbose_name='Text > Button', max_length=200, blank=True)
    #
    faq_question_1 = models.CharField(verbose_name='FAQ > Question 1', max_length=1000, blank=True)
    faq_answer_1 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 1', blank=True)
    faq_question_2 = models.CharField(verbose_name='FAQ > Question 2', max_length=1000, blank=True)
    faq_answer_2 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 2', blank=True)
    faq_question_3 = models.CharField(verbose_name='FAQ > Question 3', max_length=1000, blank=True)
    faq_answer_3 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 3', blank=True)
    faq_question_4 = models.CharField(verbose_name='FAQ > Question 4', max_length=1000, blank=True)
    faq_answer_4 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 4', blank=True)
    faq_question_5 = models.CharField(verbose_name='FAQ > Question 5', max_length=1000, blank=True)
    faq_answer_5 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 5', blank=True)
    faq_question_6 = models.CharField(verbose_name='FAQ > Question 6', max_length=1000, blank=True)
    faq_answer_6 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 6', blank=True)
    faq_question_7 = models.CharField(verbose_name='FAQ > Question 7', max_length=1000, blank=True)
    faq_answer_7 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 7', blank=True)
    faq_question_8 = models.CharField(verbose_name='FAQ > Question 8', max_length=1000, blank=True)
    faq_answer_8 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 8', blank=True)
    faq_question_9 = models.CharField(verbose_name='FAQ > Question 9', max_length=1000, blank=True)
    faq_answer_9 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 9', blank=True)
    faq_question_10 = models.CharField(verbose_name='FAQ > Question 10', max_length=1000, blank=True)
    faq_answer_10 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 10', blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=500, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > Why To Work With Us'


class SubmitReferralPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.TextField(verbose_name='Text > Title', max_length=200, blank=True)
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
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=500, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)
    #
    email_subject = models.CharField(verbose_name='Mail > Subject', max_length=300, blank=True)
    email_text = models.TextField(verbose_name='Mail > Text', blank=True)
    email_html = tinymce_models.HTMLField(verbose_name='Mail > Rich Text', blank=True)

    class Meta:
        verbose_name = 'Page > Submit A Referral'


class SubmitReferralThanksPage(BasePage):
    thanks_title = models.CharField(verbose_name='Thanks > Title', max_length=200, blank=True)
    thanks_text = models.TextField(verbose_name='Thanks > Text', blank=True)
    thanks_button = models.CharField(verbose_name='Thanks > Button', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Page > Submit A Referral Thanks'


class ApplicantsHowItWorksPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.TextField(verbose_name='Text > Title', max_length=200, blank=True)
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
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > Applicants How It Works'


class EmployerHowItWorksPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.TextField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    text_button = models.CharField(verbose_name='Text > Button', max_length=200, blank=True)
    #
    plan_title = models.CharField(verbose_name='Plan > Title', max_length=1000, blank=True)
    plan_1 = models.TextField(verbose_name='Plan > Step 1', blank=True)
    plan_2 = models.TextField(verbose_name='Plan > Step 2', blank=True)
    plan_3 = models.TextField(verbose_name='Plan > Step 3', blank=True)
    plan_4 = models.TextField(verbose_name='Plan > Step 4', blank=True)
    plan_5 = models.TextField(verbose_name='Plan > Step 5', blank=True)
    plan_button = models.CharField(verbose_name='Plan > Button', max_length=1000, blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > Employer How It Works'


class ServicesPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.TextField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    #
    courses_title = models.CharField(verbose_name='Courses > Title', blank=True, max_length=200)
    courses_text = models.TextField(verbose_name='Courses > Text', blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > Courses'


class WorkingInAustriaPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.TextField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    #
    faq_question_1 = models.CharField(verbose_name='FAQ > Question 1', max_length=1000, blank=True)
    faq_answer_1 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 1', blank=True)
    faq_question_2 = models.CharField(verbose_name='FAQ > Question 2', max_length=1000, blank=True)
    faq_answer_2 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 2', blank=True)
    faq_question_3 = models.CharField(verbose_name='FAQ > Question 3', max_length=1000, blank=True)
    faq_answer_3 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 3', blank=True)
    faq_question_4 = models.CharField(verbose_name='FAQ > Question 4', max_length=1000, blank=True)
    faq_answer_4 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 4', blank=True)
    faq_question_5 = models.CharField(verbose_name='FAQ > Question 5', max_length=1000, blank=True)
    faq_answer_5 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 5', blank=True)
    faq_question_6 = models.CharField(verbose_name='FAQ > Question 6', max_length=1000, blank=True)
    faq_answer_6 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 6', blank=True)
    faq_question_7 = models.CharField(verbose_name='FAQ > Question 7', max_length=1000, blank=True)
    faq_answer_7 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 7', blank=True)
    faq_question_8 = models.CharField(verbose_name='FAQ > Question 8', max_length=1000, blank=True)
    faq_answer_8 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 8', blank=True)
    faq_question_9 = models.CharField(verbose_name='FAQ > Question 9', max_length=1000, blank=True)
    faq_answer_9 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 9', blank=True)
    faq_question_10 = models.CharField(verbose_name='FAQ > Question 10', max_length=1000, blank=True)
    faq_answer_10 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 10', blank=True)
    faq_question_11 = models.CharField(verbose_name='FAQ > Question 11', max_length=1000, blank=True)
    faq_answer_11 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 11', blank=True)
    faq_question_12 = models.CharField(verbose_name='FAQ > Question 12', max_length=1000, blank=True)
    faq_answer_12 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 12', blank=True)
    faq_question_13 = models.CharField(verbose_name='FAQ > Question 13', max_length=1000, blank=True)
    faq_answer_13 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 13', blank=True)
    faq_question_14 = models.CharField(verbose_name='FAQ > Question 14', max_length=1000, blank=True)
    faq_answer_14 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 14', blank=True)
    faq_question_15 = models.CharField(verbose_name='FAQ > Question 15', max_length=1000, blank=True)
    faq_answer_15 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 15', blank=True)
    faq_question_16 = models.CharField(verbose_name='FAQ > Question 16', max_length=1000, blank=True)
    faq_answer_16 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 16', blank=True)
    faq_question_17 = models.CharField(verbose_name='FAQ > Question 17', max_length=1000, blank=True)
    faq_answer_17 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 17', blank=True)
    faq_question_18 = models.CharField(verbose_name='FAQ > Question 18', max_length=1000, blank=True)
    faq_answer_18 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 18', blank=True)
    faq_question_19 = models.CharField(verbose_name='FAQ > Question 19', max_length=1000, blank=True)
    faq_answer_19 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 19', blank=True)
    faq_question_20 = models.CharField(verbose_name='FAQ > Question 20', max_length=1000, blank=True)
    faq_answer_20 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 20', blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > Working In Austria'


class VideoResumePage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.TextField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    #
    benefits_left_title = models.CharField(verbose_name='Benefits > Title Left', max_length=200, blank=True)
    benefits_left_text = models.TextField(verbose_name='Benefits > Text Left', blank=True)
    benefits_center_title = models.CharField(verbose_name='Benefits > Title Center', max_length=200, blank=True)
    benefits_center_text = models.TextField(verbose_name='Benefits > Text Center', blank=True)
    benefits_right_title = models.CharField(verbose_name='Benefits > Title Right', max_length=200, blank=True)
    benefits_right_text = models.TextField(verbose_name='Benefits > Text Right', blank=True)
    #
    advantages_title = models.CharField(verbose_name='Advantages > Title', max_length=200, blank=True)
    advantages_title_1 = models.CharField(verbose_name='Advantages > Title 1', max_length=200, blank=True)
    advantages_text_1 = models.TextField(verbose_name='Advantages > Text 1', blank=True)
    advantages_title_2 = models.CharField(verbose_name='Advantages > Title 2', max_length=200, blank=True)
    advantages_text_2 = models.TextField(verbose_name='Advantages > Text 2', blank=True)
    advantages_title_3 = models.CharField(verbose_name='Advantages > Title 3', max_length=200, blank=True)
    advantages_text_3 = models.TextField(verbose_name='Advantages > Text 3', blank=True)
    advantages_title_4 = models.CharField(verbose_name='Advantages > Title 4', max_length=200, blank=True)
    advantages_text_4 = models.TextField(verbose_name='Advantages > Text 4', blank=True)
    advantages_title_5 = models.CharField(verbose_name='Advantages > Title 5', max_length=200, blank=True)
    advantages_text_5 = models.TextField(verbose_name='Advantages > Text 5', blank=True)
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
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > Video Resume'


class EmployerFaqPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.TextField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    text_button = models.CharField(verbose_name='Text > Button', max_length=200, blank=True)
    #
    faq_question_1 = models.CharField(verbose_name='FAQ > Question 1', max_length=1000, blank=True)
    faq_answer_1 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 1', blank=True)
    faq_question_2 = models.CharField(verbose_name='FAQ > Question 2', max_length=1000, blank=True)
    faq_answer_2 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 2', blank=True)
    faq_question_3 = models.CharField(verbose_name='FAQ > Question 3', max_length=1000, blank=True)
    faq_answer_3 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 3', blank=True)
    faq_question_4 = models.CharField(verbose_name='FAQ > Question 4', max_length=1000, blank=True)
    faq_answer_4 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 4', blank=True)
    faq_question_5 = models.CharField(verbose_name='FAQ > Question 5', max_length=1000, blank=True)
    faq_answer_5 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 5', blank=True)
    faq_question_6 = models.CharField(verbose_name='FAQ > Question 6', max_length=1000, blank=True)
    faq_answer_6 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 6', blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > Employer FAQ'


class JobSeekerFaqPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.TextField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    #
    faq_question_1 = models.CharField(verbose_name='FAQ > Question 1', max_length=1000, blank=True)
    faq_answer_1 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 1', blank=True)
    faq_question_2 = models.CharField(verbose_name='FAQ > Question 2', max_length=1000, blank=True)
    faq_answer_2 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 2', blank=True)
    faq_question_3 = models.CharField(verbose_name='FAQ > Question 3', max_length=1000, blank=True)
    faq_answer_3 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 3', blank=True)
    faq_question_4 = models.CharField(verbose_name='FAQ > Question 4', max_length=1000, blank=True)
    faq_answer_4 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 4', blank=True)
    faq_question_5 = models.CharField(verbose_name='FAQ > Question 5', max_length=1000, blank=True)
    faq_answer_5 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 5', blank=True)
    faq_question_6 = models.CharField(verbose_name='FAQ > Question 6', max_length=1000, blank=True)
    faq_answer_6 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 6', blank=True)
    faq_question_7 = models.CharField(verbose_name='FAQ > Question 7', max_length=1000, blank=True)
    faq_answer_7 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 7', blank=True)
    faq_question_8 = models.CharField(verbose_name='FAQ > Question 8', max_length=1000, blank=True)
    faq_answer_8 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 8', blank=True)
    faq_question_9 = models.CharField(verbose_name='FAQ > Question 9', max_length=1000, blank=True)
    faq_answer_9 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 9', blank=True)
    faq_question_10 = models.CharField(verbose_name='FAQ > Question 10', max_length=1000, blank=True)
    faq_answer_10 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 10', blank=True)
    faq_question_11 = models.CharField(verbose_name='FAQ > Question 11', max_length=1000, blank=True)
    faq_answer_11 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 11', blank=True)
    faq_question_12 = models.CharField(verbose_name='FAQ > Question 12', max_length=1000, blank=True)
    faq_answer_12 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 12', blank=True)
    faq_question_13 = models.CharField(verbose_name='FAQ > Question 13', max_length=1000, blank=True)
    faq_answer_13 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 13', blank=True)
    faq_question_14 = models.CharField(verbose_name='FAQ > Question 14', max_length=1000, blank=True)
    faq_answer_14 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 14', blank=True)
    faq_question_15 = models.CharField(verbose_name='FAQ > Question 15', max_length=1000, blank=True)
    faq_answer_15 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 15', blank=True)
    faq_question_16 = models.CharField(verbose_name='FAQ > Question 16', max_length=1000, blank=True)
    faq_answer_16 = tinymce_models.HTMLField(verbose_name='FAQ > Answer 16', blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > Job Seeker FAQ'


class StaffingSolutionsPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.TextField(verbose_name='Text > Title', max_length=1000, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=1000, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    #
    solutions_title = models.TextField(verbose_name='Solutions > Title', blank=True)
    #
    cta_title = models.CharField(verbose_name='Cta > Title', max_length=1000, blank=True)
    cta_text = models.TextField(verbose_name='Cta > Text', blank=True)
    cta_button = models.CharField(verbose_name='Cta > Button', max_length=1000, blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > Staffing Solutions'


class SubmitPositionPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    form_title = models.CharField(verbose_name='Form > Title', max_length=1000, blank=True)
    form_text = tinymce_models.HTMLField(verbose_name='Form > Text', blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)
    #
    email_subject = models.CharField(verbose_name='Mail > Subject', max_length=300, blank=True)
    email_text = models.TextField(verbose_name='Mail > Text', blank=True)
    email_html = tinymce_models.HTMLField(verbose_name='Mail > Rich Text', blank=True)

    class Meta:
        verbose_name = 'Page > Submit A Position'


class SubmitPositionThanksPage(BasePage):
    thanks_title = models.CharField(verbose_name='Thanks > Title', max_length=200, blank=True)
    thanks_text = models.TextField(verbose_name='Thanks > Text', blank=True)
    thanks_button = models.CharField(verbose_name='Thanks > Button', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Page > Submit A Position Thanks'


class InitiativeApplicationPage(BasePage):
    header_title = models.TextField(verbose_name='Header > Title', max_length=200, blank=True)
    header_text = tinymce_models.HTMLField(verbose_name='Header > Text', blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)
    #
    email_subject = models.CharField(verbose_name='Mail > Subject', max_length=300, blank=True)
    email_text = models.TextField(verbose_name='Mail > Text', blank=True)
    email_html = tinymce_models.HTMLField(verbose_name='Mail > Rich Text', blank=True)

    class Meta:
        verbose_name = 'Page > Initiative Application'


class InitiativeApplicationThanksPage(BasePage):
    thanks_title = models.CharField(verbose_name='Thanks > Title', max_length=200, blank=True)
    thanks_text = models.TextField(verbose_name='Thanks > Text', blank=True)
    thanks_button = models.CharField(verbose_name='Thanks > Button', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Page > Initiative Application Thanks'


class AboutPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    text_title = models.TextField(verbose_name='Text > Title', max_length=200, blank=True)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200, blank=True)
    text_text = tinymce_models.HTMLField(verbose_name='Text > Text', blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > About'


class PortalPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > Portal'


class ContactPage(BasePage):
    #
    header_title = models.TextField(verbose_name='Header > Title', max_length=1000, blank=True)
    #
    form_title = models.CharField(verbose_name='Form > Title', max_length=1000, blank=True)
    form_text = tinymce_models.HTMLField(verbose_name='Form > Text', blank=True)
    #
    quote_text = models.TextField(verbose_name='Quote > Text', blank=True)
    quote_author = models.CharField(verbose_name='Quote > Author', max_length=200, blank=True)
    quote_size = models.CharField(verbose_name='Quote > Size', choices=SIZE_CHOICES, max_length=100, default='NORMAL',
                                  blank=True)

    class Meta:
        verbose_name = 'Page > Contact'


class ContactThanksPage(BasePage):
    #
    thanks_title = models.CharField(verbose_name='Thanks > Title', max_length=200, blank=True)
    thanks_text = models.TextField(verbose_name='Thanks > Text', blank=True)
    thanks_button = models.CharField(verbose_name='Thanks > Button', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Page > Contact Thanks'


class ImprintPage(BasePage):
    pre = models.CharField(verbose_name='Pre', max_length=1000, blank=True)
    title = models.CharField(verbose_name='Title', max_length=1000, blank=True)
    text = tinymce_models.HTMLField(verbose_name='Text', blank=True)

    class Meta:
        verbose_name = 'Page > Imprint'


class AgbPage(BasePage):
    pre = models.CharField(verbose_name='Pre', max_length=1000, blank=True)
    title = models.CharField(verbose_name='Title', max_length=1000, blank=True)
    text = tinymce_models.HTMLField(verbose_name='Text', blank=True)

    class Meta:
        verbose_name = 'Page > Agb'


class PrivacyPage(BasePage):
    pre = models.CharField(verbose_name='Pre', max_length=1000, blank=True)
    title = models.CharField(verbose_name='Title', max_length=1000, blank=True)
    text = tinymce_models.HTMLField(verbose_name='Text', blank=True)

    class Meta:
        verbose_name = 'Page > Privacy'
