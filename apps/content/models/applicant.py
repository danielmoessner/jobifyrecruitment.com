from django.utils.translation import gettext_lazy as _
from apps.content.models import StaffCategory
from django.utils import timezone
from django.db import models


class Applicant(models.Model):
    # choices
    SALUTATION_CHOICES = (
        ('M', _('Herr')),
        ('F', _('Frau')),
        ('D', _('Divers')),
    )
    MARITAL_STATUS_CHOICES = (
        ('SINGLE', _('Ledig')),
        ('DIVORCED', _('Geschieden')),
        ('SEPERATED', _('Getrennt lebend')),
        ('MARRIED', _('Verheiratet')),
        ('WIDOWED', _('Verwitwet'))
    )
    LANGUAGE_KNOWLEDGE_CHOICES = (
        ('MOTHER', _('Mother tongue')),
        ('FLUENT', _('Fluent')),
        ('GOOD', _('Good')),
        ('BASIC', _('Basic')),
    )
    EXPERIENCE_CHOICES = (
        ('1', _('1 Year')),
        ('5', _('1 to 5 Years')),
        ('10', _('5 to 10 Years')),
        ('MAX', _('More Than 10 Years')),
    )
    # contact details
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='content/applicant/photo/')
    salutation = models.CharField(verbose_name=_('Salutation'), choices=SALUTATION_CHOICES, max_length=1)
    firstname = models.CharField(_('Firstname'), max_length=100)
    lastname = models.CharField(_('Lastname'), max_length=100)
    street = models.CharField(_('Street'), max_length=100)
    number = models.CharField(_('Number'), max_length=10)
    postal = models.CharField(_('Postal Code'), max_length=10)
    city = models.CharField(_('City'), max_length=50)
    country = models.CharField(_('Country'), max_length=100)
    phone = models.CharField(_('Phone'), max_length=20)
    email = models.EmailField(_('E-Mail'))
    # personal information
    birthday = models.DateField(verbose_name=_('Birthday'))
    nationality = models.CharField(_('Nationality'), max_length=100)
    marital_status = models.CharField(_('Marital Status'), max_length=20, choices=MARITAL_STATUS_CHOICES)
    # language skills
    language1 = models.CharField(max_length=50)
    language1knowledge = models.CharField(max_length=50, choices=LANGUAGE_KNOWLEDGE_CHOICES)
    language2 = models.CharField(max_length=50, blank=True)
    language2knowledge = models.CharField(max_length=50, choices=LANGUAGE_KNOWLEDGE_CHOICES, blank=True)
    language3 = models.CharField(max_length=50, blank=True)
    language3knowledge = models.CharField(max_length=50, choices=LANGUAGE_KNOWLEDGE_CHOICES, blank=True)
    language4 = models.CharField(max_length=50, blank=True)
    language4knowledge = models.CharField(max_length=50, choices=LANGUAGE_KNOWLEDGE_CHOICES, blank=True)
    # career
    department = models.ForeignKey(StaffCategory, verbose_name=_('Department'), on_delete=models.PROTECT,
                                   related_name='applicants')
    experience = models.CharField(_('Experience'), choices=EXPERIENCE_CHOICES, max_length=100)
    position = models.CharField(_('Position'), max_length=50)
    employer = models.CharField(_('Employer'), max_length=50)
    from_date = models.DateField(_('From Date'))
    until_date = models.DateField(_('Until Date'))
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
