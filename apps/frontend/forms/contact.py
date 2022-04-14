from crispy_forms.layout import Submit, Layout, Row, Field
from crispy_forms.helper import FormHelper
from django import forms


class ContactForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    company = forms.CharField()
    street = forms.CharField()
    postal_code = forms.CharField()
    city = forms.CharField()
    INTEREST_CHOICES = (
        ('JOB_FIND', 'Job finden'),
        ('JOB_SEARCH', 'Job suchen'),
        ('REFERRAL_PROGRAM', 'Empfehlungsprogramm'),
        ('EDUCATION', 'Weiterbildungen / Webinaren'),
        ('RECRUITING', 'Internationaler Rekrutierung'),
        ('VIDEO', 'Video-Recruiting'),
        ('PARTNER', 'Partner werden'),
        ('LEGAL', 'Rechtliches')
    )
    interest = forms.ChoiceField(choices=INTEREST_CHOICES)
    message = forms.CharField(widget=forms.Textarea())
    privacy = forms.BooleanField(label='Datenschutzhinweis: Selbstverständlich werden Ihre Daten vertraulich behandelt '
                                       'und erst nach Ihrer Zustimmung an Dritte weitergegeben. Ja, ich erkläre mich '
                                       'mit den Datenschutzbestimmungen einverstanden.')
    privacy_label = 'Datenschutzhinweis: Selbstverständlich werden Ihre Daten vertraulich behandelt und erst nach ' \
                    'Ihrer Zustimmung an Dritte weitergegeben. Ja, ich erkläre mich mit den Datenschutzbestimmungen ' \
                    'einverstanden.'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'djangoform'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': True}
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Row('firstname', 'lastname'),
            Row('email', 'phone'),
            Row('company', 'street'),
            Row('postal_code', 'city'),
            'interest',
            'message',
            Field('privacy'),
        )
