from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.views.generic import TemplateView

from apps.applicants.forms import ApplicantForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class InitiativeApplicationView(FormMixin, TemplateView):
    template_name = 'initiative_application.html'
    form_class = ApplicantForm
