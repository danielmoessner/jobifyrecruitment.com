from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from crispy_forms.layout import Layout, Row, Submit, HTML, Field
from apps.content.static import LANGUAGE_CHOICES, PRIVACY_LABEL
from crispy_forms.helper import FormHelper
from apps.content.models import Applicant
from django import forms


class ApplicantForm(forms.ModelForm):
    privacy = forms.BooleanField(label=PRIVACY_LABEL)
    birthday = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('Birthday'))
    from_date = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('From Date'))
    until_date = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('Until Date'))
    country = CountryField().formfield(label=_('Country'))
    # language1 = CountryField().formfield()
    language1 = forms.ChoiceField(choices=LANGUAGE_CHOICES)
    language2 = CountryField().formfield()
    language3 = CountryField().formfield()
    language4 = CountryField().formfield()

    class Meta:
        model = Applicant
        fields = '__all__'
        labels = {
            'country': _('Country')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'djangoform'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': True}
        self.helper.add_input(Submit('submit', _('Submit')))
        self.helper.layout = Layout(
            HTML('<h2>{}</h2>'.format(_('Contact details'))),
            'photo',
            Row('salutation', 'firstname', 'lastname'),
            Row('street', 'number'),
            Row('postal', 'city'),
            'country',
            Row('email', 'phone'),
            HTML('<h2 class="mt-16">{}</h2>'.format(_('Personal Information'))),
            Row('birthday', 'nationality', 'marital_status'),
            HTML('<h2 class="mt-16">{}</h2>'.format(_('Language skill'))),
            Row('language1', 'language1knowledge'),
            Row('language2', 'language2knowledge'),
            Row('language3', 'language3knowledge'),
            Row('language4', 'language4knowledge'),
            HTML('<h2 class="mt-16">{}</h2>'.format(_('Professional career'))),
            Row('department', 'experience'),
            Row('position', 'employer'),
            Row('from_date', 'until_date'),
            HTML('<h2 class="mt-16">{}</h2>'.format(_('Additional information'))),
            'cv',
            'more',
            HTML('<h2 class="mt-16">{}</h2>'.format(_('Privacy'))),
            Field('privacy'),
        )
