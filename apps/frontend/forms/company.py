from crispy_forms.layout import Submit, Layout, Row, Field
from crispy_forms.helper import FormHelper
from apps.content.models import Company
from django import forms


class CompanyForm(forms.ModelForm):
    privacy = forms.BooleanField(label='Datenschutzhinweis: Selbstverständlich werden Ihre Daten vertraulich behandelt '
                                       'und erst nach Ihrer Zustimmung an Dritte weitergegeben. Ja, ich erkläre mich '
                                       'mit den Datenschutzbestimmungen einverstanden.')
    privacy_label = 'Datenschutzhinweis: Selbstverständlich werden Ihre Daten vertraulich behandelt und erst nach ' \
                    'Ihrer Zustimmung an Dritte weitergegeben. Ja, ich erkläre mich mit den Datenschutzbestimmungen ' \
                    'einverstanden.'
    job_start = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'job_start': forms.DateTimeInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'djangoform'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': True}
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            'manager_name',
            Row('company_name', 'company_email'),
            'job',
            Row('looking_for', 'job_position'),
            Row('job_duration', 'job_start'),
            'job_description',
            Field('privacy'),
        )
