from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from apps.content.static import LANGUAGE_CHOICES, PRIVACY_LABEL, NATIONALITY_CHOICES
from crispy_forms.layout import Layout, Row, Submit, HTML, Field
from crispy_forms.helper import FormHelper
from apps.content.models import Applicant
from django import forms


class ApplicantForm(forms.ModelForm):
    privacy = forms.BooleanField(label=PRIVACY_LABEL)
    birthday = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('Birthday'))
    from_date = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('From Date'))
    until_date = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('Until Date'))
    nationality = forms.ChoiceField(choices=NATIONALITY_CHOICES, label=_('Nationality'))
    country = CountryField().formfield(label=_('Country'))
    language1 = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=False, label=_('Language'))
    language2 = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=False, label=_('Language'))
    language3 = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=False, label=_('Language'))
    language4 = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=False, label=_('Language'))

    class Meta:
        model = Applicant
        exclude = ['show']
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
            HTML('<h2>{}</h2>'.format(_('Personal details'))),
            Row('wanted_job_title', 'photo'),

            HTML('<h2 class="mt-16">{}</h2><p>{}</p>'.format(_("What's the best way for employers to contact you?"),
                                               _("We suggest including an email and phone number."))),
            Row('firstname', 'lastname'),
            'profession',
            Row('city', 'state_province', 'postal'),

            Row('email', 'phone'),

            HTML('<h2 class="mt-16">{}</h2>'.format(_('Personal Information'))),
            Row('birthday', 'nationality', 'marital_status'),

            HTML('<h2 class="mt-16">{}</h2>'.format(_('Language skill'))),
            Row('language1', 'language1knowledge'),
            Row('language2', 'language2knowledge'),
            Row('language3', 'language3knowledge'),
            Row('language4', 'language4knowledge'),

            HTML('<h2 class="mt-16">{}</h2>'.format(_('Tell us about your education'))),
            Row('school_name', 'school_location'),
            'degree',
            Row('field_of_study', 'graduation_start_date', 'graduation_end_date'),
            'currently_attend_school',

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
