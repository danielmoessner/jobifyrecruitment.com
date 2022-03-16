from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.utils.translation import gettext_lazy as _
from apps.applicants.forms import ApplicantForm
from django.views.generic import TemplateView

from apps.companies.forms import CompanyForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('English')
        return context


class InitiativeApplicationView(FormMixin, TemplateView):
    template_name = 'initiative_application.html'
    form_class = ApplicantForm


class ForCompaniesView(TemplateView):
    template_name = 'for_companies.html'


class CompanyFormView(FormMixin, TemplateView):
    template_name = 'company_form.html'
    form_class = CompanyForm


class ForApplicantsView(TemplateView):
    template_name = 'for_applicants.html'


class PortalView(TemplateView):
    template_name = 'portal.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class ImprintView(TemplateView):
    template_name = 'imprint.html'


class PrivacyView(TemplateView):
    template_name = 'privacy.html'
