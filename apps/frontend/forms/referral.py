from django.utils.translation import gettext_lazy as _
from crispy_forms.layout import Submit, Layout, Field
from apps.content.static import PRIVACY_LABEL
from crispy_forms.helper import FormHelper
from apps.content.models import Referral
from django import forms


class ReferralForm(forms.ModelForm):
    privacy = forms.BooleanField(label=PRIVACY_LABEL)

    class Meta:
        model = Referral
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'djangoform'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': True}
        self.helper.add_input(Submit('submit', _('Submit')))
        self.helper.layout = Layout(
            'your_name',
            'your_email',
            'referral_name',
            'referral_email',
            'referral_phone',
            'referral_job',
            'referral_resume',
            Field('privacy'),
        )
