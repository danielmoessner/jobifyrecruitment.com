from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.utils.translation import gettext_lazy as _
from apps.applicants.forms import ApplicantForm
from django.views.generic import TemplateView
from apps.referrals.forms import ReferralForm
from apps.companies.forms import CompanyForm
from apps.content.models import WhyToWorkWithUsPage, Service


###
# context
###
class BaseContext:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


class PageContext:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = self.page.get_solo()
        return context


###
# views
###
class IndexView(BaseContext, LoginRequiredMixin, TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('English')
        return context


class InitiativeApplicationView(BaseContext, FormMixin, TemplateView):
    template_name = 'initiative_application/initiative_application.html'
    form_class = ApplicantForm


class ForCompaniesView(BaseContext, TemplateView):
    template_name = 'for_companies/for_companies.html'


class CompanyFormView(BaseContext, FormMixin, TemplateView):
    template_name = 'company_form/company_form.html'
    form_class = CompanyForm


class WhyWorkWithUsView(BaseContext, PageContext, TemplateView):
    template_name = 'why_work_with_us/why_work_with_us.html'
    page = WhyToWorkWithUsPage


class SubmitReferralView(BaseContext, FormMixin, TemplateView):
    template_name = 'submit_a_referral/submit_a_referral.html'
    form_class = ReferralForm


class ApplicantsHowItWorksView(BaseContext, TemplateView):
    template_name = 'applicants_how_it_works/applicants_how_it_works.html'


class WorkingInAustriaView(BaseContext, TemplateView):
    template_name = 'working_in_austria/index.html'


class ServicesView(BaseContext, TemplateView):
    template_name = 'services/index.html'


class PortalView(BaseContext, TemplateView):
    template_name = 'portal/portal.html'


###
# both
###
class ContactView(BaseContext, TemplateView):
    template_name = 'contact/contact.html'


class VideoResumeView(BaseContext, TemplateView):
    template_name = 'video_resume/video_resume.html'


###
# other
###
class ImprintView(BaseContext, TemplateView):
    template_name = 'imprint/imprint.html'


class PrivacyView(BaseContext, TemplateView):
    template_name = 'privacy/privacy.html'
