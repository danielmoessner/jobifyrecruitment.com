from crispy_forms.layout import Layout, Row, Submit, HTML, Field
from crispy_forms.helper import FormHelper
from apps.content.models import Applicant
from django import forms


class ApplicantForm(forms.ModelForm):
    privacy = forms.BooleanField(label='Datenschutzhinweis: Selbstverständlich werden Ihre Daten vertraulich behandelt '
                                       'und erst nach Ihrer Zustimmung an Dritte weitergegeben. Ja, ich erkläre mich '
                                       'mit den Datenschutzbestimmungen einverstanden.')
    privacy_label = 'Datenschutzhinweis: Selbstverständlich werden Ihre Daten vertraulich behandelt und erst nach ' \
                    'Ihrer Zustimmung an Dritte weitergegeben. Ja, ich erkläre mich mit den Datenschutzbestimmungen ' \
                    'einverstanden.'
    birthday = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    from_date = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    until_date = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Applicant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'djangoform'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': True}
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            HTML('<h2>Contact details</h2>'),
            'photo',
            Row('salutation', 'firstname', 'lastname'),
            Row('street', 'number'),
            Row('postal', 'city'),
            'country',
            Row('email', 'phone'),
            HTML('<h2 class="mt-16">Personal Information</h2>'),
            Row('birthday', 'nationality', 'marital_status'),
            HTML('<h2 class="mt-16">Language skill</h2>'),
            Row('language1', 'language1knowledge'),
            Row('language2', 'language2knowledge'),
            Row('language3', 'language3knowledge'),
            Row('language4', 'language4knowledge'),
            HTML('<h2 class="mt-16">Professional career</h2>'),
            Row('position', 'employer'),
            Row('from_date', 'until_date'),
            HTML('<h2 class="mt-16">Additional information</h2>'),
            'cv',
            'more',
            HTML('<h2 class="mt-16">Privacy</h2>'),
            Field('privacy', css_class='w-6 h-6 mr-2 flex-shrink-0'),
        )
