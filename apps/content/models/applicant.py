from django.utils.translation import gettext_lazy as _
from apps.content.models import StaffCategory
from django.utils import timezone
from django.db import models


class Applicant(models.Model):
    # choices
    SALUTATION_CHOICES = (
        ('M', _('Mr.')),
        ('F', _('Mrs.')),
        ('D', _('Diverse')),
    )
    MARITAL_STATUS_CHOICES = (
        ('SINGLE', _('Single')),
        ('DIVORCED', _('Divorced')),
        ('SEPERATED', _('Separated')),
        ('MARRIED', _('Married')),
        ('WIDOWED', _('Widowed'))
    )
    LANGUAGE_KNOWLEDGE_CHOICES = (
        ('MOTHER', _('Mother tongue')),
        ('FLUENT', _('Fluent in spoken and written')),
        ('GOOD', _('Good knowledge written and spoken')),
        ('BASIC', _('Basic knowledge')),
    )
    EXPERIENCE_CHOICES = (
        ('1', _('1 Year')),
        ('5', _('1 to 5 Years')),
        ('10', _('5 to 10 Years')),
        ('MAX', _('More Than 10 Years')),
    )
    # admin
    show = models.BooleanField(default=False)
    # contact details
    wanted_job_title = models.CharField(_('Wanted Job Title'), max_length=200)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='content/applicant/photo/')
    salutation = models.CharField(verbose_name=_('Salutation'), choices=SALUTATION_CHOICES, max_length=1)
    firstname = models.CharField(_('Firstname'), max_length=100)
    lastname = models.CharField(_('Lastname'), max_length=100)
    country = models.CharField(_('Country'), max_length=100)
    # profession = models.CharField(_('Profession'), max_length=200)
    # street = models.CharField(_('Street'), max_length=100)
    # number = models.CharField(_('Number'), max_length=10)
    # city = models.CharField(_('City'), max_length=50)
    # state_province = models.CharField(_('State / Province'), max_length=100)
    # postal = models.CharField(_('Zip Code'), max_length=10)
    # country = models.CharField(_('Country'), max_length=100)
    phone = models.CharField(_('Phone'), max_length=20)
    email = models.EmailField(_('E-Mail'))
    # personal information
    birthday = models.DateField(verbose_name=_('Birthday'))
    nationality = models.CharField(_('Nationality'), max_length=100)
    marital_status = models.CharField(_('Marital Status'), max_length=20, choices=MARITAL_STATUS_CHOICES)
    # language skills
    language1 = models.CharField(_('Language'), max_length=50, blank=False)
    language1knowledge = models.CharField(_('Knowledge'), max_length=50, choices=LANGUAGE_KNOWLEDGE_CHOICES)
    language2 = models.CharField(_('Language'), max_length=50, blank=True)
    language2knowledge = models.CharField(_('Knowledge'), max_length=50, choices=LANGUAGE_KNOWLEDGE_CHOICES, blank=True)
    language3 = models.CharField(_('Language'), max_length=50, blank=True)
    language3knowledge = models.CharField(_('Knowledge'), max_length=50, choices=LANGUAGE_KNOWLEDGE_CHOICES, blank=True)
    language4 = models.CharField(_('Language'), max_length=50, blank=True)
    language4knowledge = models.CharField(_('Knowledge'), max_length=50, choices=LANGUAGE_KNOWLEDGE_CHOICES, blank=True)
    # education
    school_name = models.CharField(_('School Name'), max_length=200)
    school_location = models.CharField(_('School Location'), max_length=200)
    degree = models.CharField(_('Degree'), max_length=200)
    field_of_study = models.CharField(_('Field of Study'), max_length=200)
    graduation_start_date = models.DateField(_('Graduation Start Date'))
    graduation_end_date = models.DateField(_('Graduation End Date'), blank=True)
    currently_attend_school = models.BooleanField(_('I currently attend here'))
    # career
    department = models.ForeignKey(StaffCategory, verbose_name=_('Department'), on_delete=models.PROTECT,
                                   related_name='applicants')
    experience = models.CharField(_('Experience'), choices=EXPERIENCE_CHOICES, max_length=100)
    #
    position = models.CharField(_('Position'), max_length=50, blank=True)
    employer = models.CharField(_('Employer'), max_length=50, blank=True)
    from_date = models.DateField(_('From Date'), blank=True)
    until_date = models.DateField(_('Until Date'), blank=True)
    position_2 = models.CharField(_('Position'), max_length=50, null=True, blank=True)
    employer_2 = models.CharField(_('Employer'), max_length=50, null=True, blank=True)
    from_date_2 = models.DateField(_('From Date'), null=True, blank=True)
    until_date_2 = models.DateField(_('Until Date'), null=True, blank=True)
    position_3 = models.CharField(_('Position'), max_length=50, null=True, blank=True)
    employer_3 = models.CharField(_('Employer'), max_length=50, null=True, blank=True)
    from_date_3 = models.DateField(_('From Date'), null=True, blank=True)
    until_date_3 = models.DateField(_('Until Date'), null=True, blank=True)
    # cv
    cv = models.FileField(_('CV'), upload_to='applicants/applicant/cv/')
    more = models.FileField(_('More'), upload_to='applicants/applicant/more/', blank=True)
    # other
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Applicant'
        verbose_name_plural = 'Applicants'

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)

    @property
    def name(self):
        return '{} {}'.format(self.firstname, self.lastname)

    @property
    def age(self):
        return int((timezone.now().date() - self.birthday).days / 365.25)
