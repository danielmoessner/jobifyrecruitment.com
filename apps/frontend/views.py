from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormView
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from apps.content.models import WhyToWorkWithUsPage, Service, SubmitReferralPage, StaffCategory, \
    ApplicantsHowItWorksPage, WorkingInAustriaPage, EmployerFaqPage, StaffingSolutionsPage, VideoResumePage, \
    SubmitPositionPage, ServicesPage, SubmitReferralThanksPage, InitiativeApplicationThanksPage, \
    SubmitPositionThanksPage, AboutPage, Company, Applicant, Referral, MemberCategory, PortalPage, ContactPage, \
    ImprintPage, ContactThanksPage
from django.urls import reverse_lazy
from .forms import ApplicantForm, CompanyForm, ReferralForm, ContactForm


###
# context
###
class BaseContext:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['staff_categories'] = StaffCategory.objects.all()
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
        context['applicants'] = Applicant.objects.all()
        return context


class InitiativeApplicationView(BaseContext, CreateView):
    template_name = 'initiative_application/initiative_application.html'
    form_class = ApplicantForm
    model = Applicant
    success_url = reverse_lazy('frontend:initiative_application_thanks')


class InitiativeApplicationThanksView(BaseContext, PageContext, TemplateView):
    template_name = 'initiative_application/thanks.html'
    page = InitiativeApplicationThanksPage


class StaffingSolutionsView(BaseContext, PageContext, TemplateView):
    template_name = 'staffing_solutions/index.html'
    page = StaffingSolutionsPage


class SubmitPositionView(BaseContext, PageContext, CreateView):
    template_name = 'submit_a_position/index.html'
    form_class = CompanyForm
    page = SubmitPositionPage
    model = Company
    success_url = reverse_lazy('frontend:submit_a_position_thanks')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(initial={'looking_for': self.request.GET.get('expertise')})
        return kwargs


class SubmitPositionThanksView(BaseContext, PageContext, TemplateView):
    template_name = 'submit_a_position/thanks.html'
    page = SubmitPositionThanksPage


class EmployerFaqsView(BaseContext, PageContext, TemplateView):
    template_name = 'employer_faqs/index.html'
    page = EmployerFaqPage


class WhyWorkWithUsView(BaseContext, PageContext, TemplateView):
    template_name = 'why_work_with_us/index.html'
    page = WhyToWorkWithUsPage


class SubmitReferralView(BaseContext, PageContext, CreateView):
    template_name = 'submit_a_referral/index.html'
    form_class = ReferralForm
    page = SubmitReferralPage
    model = Referral
    success_url = reverse_lazy('frontend:submit_a_referral_thanks')


class SubmitReferralThanksView(BaseContext, PageContext, TemplateView):
    template_name = 'submit_a_referral/thanks.html'
    page = SubmitReferralThanksPage


class ApplicantsHowItWorksView(BaseContext, PageContext, TemplateView):
    template_name = 'applicants_how_it_works/index.html'
    page = ApplicantsHowItWorksPage


class WorkingInAustriaView(BaseContext, PageContext, TemplateView):
    template_name = 'working_in_austria/index.html'
    page = WorkingInAustriaPage


class ServicesView(BaseContext, PageContext, TemplateView):
    template_name = 'services/index.html'
    page = ServicesPage


class PortalView(BaseContext, PageContext, TemplateView):
    template_name = 'portal/index.html'
    page = PortalPage

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['applicants'] = Applicant.objects.all()
        context['experience_choices'] = Applicant.EXPERIENCE_CHOICES
        return context


###
# both
###
class ContactView(BaseContext, PageContext, FormView):
    template_name = 'contact/index.html'
    page = ContactPage
    form_class = ContactForm
    success_url = reverse_lazy('frontend:contact_thanks')


class ContactThanksView(BaseContext, PageContext, TemplateView):
    template_name = 'contact/thanks.html'
    page = ContactThanksPage


class VideoResumeView(BaseContext, PageContext, TemplateView):
    template_name = 'video_resume/index.html'
    page = VideoResumePage


class AboutView(BaseContext, PageContext, TemplateView):
    template_name = 'about/index.html'
    page = AboutPage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member_categories'] = MemberCategory.objects.all()
        return context


###
# other
###
class ImprintView(BaseContext, PageContext, TemplateView):
    template_name = 'imprint/index.html'
    page = ImprintPage


class PrivacyView(BaseContext, TemplateView):
    template_name = 'privacy/privacy.html'
