from django.utils.translation import gettext_lazy as _
from crispy_forms.layout import Submit, Layout, Row, Field
from apps.content.static import PRIVACY_LABEL
from crispy_forms.helper import FormHelper
from django import forms


class ContactForm(forms.Form):
    firstname = forms.CharField(label=_('Firstname'))
    lastname = forms.CharField(label=_('Lastname'))
    email = forms.EmailField(label=_('E-Mail'))
    phone = forms.CharField(label=_('Phone'))
    company = forms.CharField(label=_('Company'))
    street = forms.CharField(label=_('Street'))
    postal_code = forms.CharField(label=_('Postal Code'))
    city = forms.CharField(label=_('City'))
    INTEREST_CHOICES = (
        ('JOB_FIND', _('Find a job')),
        ('APPLICANT_FIND', _('Find a applicant')),
        ('REFERRAL_PROGRAM', _('Referral Program')),
        ('EDUCATION', _('Further training / webinars')),
        ('RECRUITING', _('International recruiting')),
        ('VIDEO', _('Video-Recruiting')),
        ('PARTNER', _('Become a partner')),
        ('LEGAL', _('Legal'))
    )
    interest = forms.ChoiceField(choices=INTEREST_CHOICES, label=_('Interest'))
    message = forms.CharField(widget=forms.Textarea(), label=_('Message'))
    privacy = forms.BooleanField(label=PRIVACY_LABEL)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'djangoform'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': True}
        self.helper.add_input(Submit('submit', _('Submit')))
        self.helper.layout = Layout(
            Row('firstname', 'lastname'),
            Row('email', 'phone'),
            Row('company', 'street'),
            Row('postal_code', 'city'),
            'interest',
            'message',
            Field('privacy'),
        )
