from django.utils import timezone
from django.utils.translation import gettext_lazy as _
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
    # contact details
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='content/applicant/photo/')
    salutation = models.CharField(verbose_name=_('Salutation'), choices=SALUTATION_CHOICES, max_length=1)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    postal = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    # personal information
    birthday = models.DateField()
    nationality = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES)
    # language skills
    language1 = models.CharField(max_length=50)
    language1knowledge = models.CharField(max_length=20)
    language2 = models.CharField(max_length=50, blank=True)
    language2knowledge = models.CharField(max_length=20, blank=True)
    language3 = models.CharField(max_length=50, blank=True)
    language3knowledge = models.CharField(max_length=20, blank=True)
    language4 = models.CharField(max_length=50, blank=True)
    language4knowledge = models.CharField(max_length=20, blank=True)
    # career
    position = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)
    from_date = models.DateField()
    until_date = models.DateField()
    # cv
    cv = models.FileField(upload_to='applicants/applicant/cv/')
    more = models.FileField(upload_to='applicants/applicant/more/', blank=True)
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
