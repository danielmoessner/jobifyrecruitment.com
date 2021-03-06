from django.utils.translation import gettext_lazy as _
from apps.content.static import LANGUAGE_CHOICES, PRIVACY_LABEL, NATIONALITY_CHOICES
from crispy_forms.layout import Layout, Row, Submit, HTML, Field
from crispy_forms.helper import FormHelper
from apps.content.models import Applicant
from django import forms


class ApplicantForm(forms.ModelForm):
    privacy = forms.BooleanField(label=PRIVACY_LABEL)
    birthday = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('Birthday'))
    from_date = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('From Date'),
                                required=False)
    until_date = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('Until Date'),
                                 required=False)

    from_date_2 = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('From Date'),
                                  required=False)
    until_date_2 = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('Until Date'),
                                   required=False)

    from_date_3 = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('From Date'),
                                  required=False)
    until_date_3 = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label=_('Until Date'),
                                   required=False)

    graduation_start_date = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}),
                                            label=_('Graduation Start Date'))
    graduation_end_date = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}),
                                          label=_('Graduation End Date'), required=False)
    nationality = forms.ChoiceField(choices=NATIONALITY_CHOICES, label=_('Nationality'))
    country = forms.ChoiceField(choices=NATIONALITY_CHOICES, label=_('Country'))
    language1 = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=True, label=_('Language'))
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

        error = """
        <span class="text-red-700">
        {% for error in form.errors.photo %}
            {{ error }}
        {% endfor %}
        </span>
        """

        photo_input = HTML("""
        <div>
        <div class="control-group flex items-end justify-start">
            <input type="file" name="photo" accept="image/*" class="!sr-only" required="" id="id_photo">
            <label for="id_photo" class="!flex items-center space-x-2 cursor-pointer">
                <img src="/static/icon/photo-input.jpg" alt="Icon" class="w-16 h-16" />
                <span class="text-gray-700">{text}</span>
            </label>
        </div>
            {error}
        </div>
        """.format(text=_('Upload photo'), error=error))

        self.helper.layout = Layout(
            HTML('<h2>{}</h2>'.format(_('Personal details'))),
            Row('wanted_job_title', photo_input),

            HTML('<h2 class="mt-16">{}</h2><p>{}</p>'.format(_("What's the best way for employers to contact you?"),
                                                             _("We suggest including an email and phone number."))),
            Row('salutation', 'firstname'),
            Row('lastname', 'country'),
            # 'profession',
            # Row('city', 'state_province', 'postal'),

            Row('email', 'phone'),

            HTML('<h2 class="mt-16">{}</h2>'.format(_('Personal Information'))),
            Row('birthday', 'nationality', 'marital_status'),

            HTML('<h2 class="mt-16">{}</h2>'.format(_('Language skill'))),
            Row('language1', 'language1knowledge'),
            Row('language2', 'language2knowledge'),
            Row('language3', 'language3knowledge'),
            Row('language4', 'language4knowledge'),

            HTML('<h2 class="mt-16">{}</h2><p>{}</p>'.format(
                _('Tell us about your education'),
                _('Please state your highest qualification or the one of equal rank.')
            )),
            Row('school_name', 'school_location'),
            Row('degree', 'field_of_study'),
            Row('graduation_start_date', 'graduation_end_date'),
            'currently_attend_school',

            HTML('<h2 class="mt-16">{}</h2><p>{}</p>'.format(
                _('Professional career'),
                _('Please start with your current position and then list 3 previous positions (if any).')
            )),
            Row('department', 'experience'),

            HTML('<div class="h-4"></div>'),
            Row('from_date', 'until_date'),
            Row('position', 'employer'),

            HTML('<div class="h-4"></div>'),
            Row('from_date_2', 'until_date_2'),
            Row('position_2', 'employer_2'),

            HTML('<div class="h-4"></div>'),
            Row('from_date_3', 'until_date_3'),
            Row('position_3', 'employer_3'),

            HTML('<h2 class="mt-16">{}</h2>'.format(_('Additional information'))),
            'cv',
            'more',
            HTML('<h2 class="mt-16">{}</h2>'.format(_('Privacy'))),
            Field('privacy'),
        )

    def _clean_date(self, name):
        value = self.cleaned_data[name]
        if value == '':
            return None
        return value

    def clean_graduation_end_date(self):
        return self._clean_date('graduation_end_date')

    def clean_until_date(self):
        return self._clean_date('until_date')

    def clean_until_date_2(self):
        return self._clean_date('until_date_2')

    def clean_until_date_3(self):
        return self._clean_date('until_date_3')

    def clean_from_date(self):
        return self._clean_date('from_date')

    def clean_from_date_2(self):
        return self._clean_date('from_date_2')

    def clean_from_date_3(self):
        return self._clean_date('from_date_3')
