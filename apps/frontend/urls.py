from django.utils.translation import gettext_lazy as _
from apps.frontend import views
from django.urls import path

app_name = "frontend"

urlpatterns = [
    # index
    path('', views.IndexView.as_view(), name='index'),
    # job seeker
    path(_('initiative-application/'), views.InitiativeApplicationView.as_view(), name='initiative_application'),
    path(_('initiative-application/thanks/'), views.InitiativeApplicationThanksView.as_view(),
         name='initiative_application_thanks'),
    path(_('why-work-with-us/'), views.WhyWorkWithUsView.as_view(), name='why_work_with_us'),
    path(_('submit-a-referral/'), views.SubmitReferralView.as_view(), name='submit_a_referral'),
    path(_('submit-a-referral/thanks/'), views.SubmitReferralThanksView.as_view(), name='submit_a_referral_thanks'),
    path(_('applicants-how-it-works/'), views.ApplicantsHowItWorksView.as_view(), name='applicants_how_it_works'),
    path(_('working-in-austria/'), views.WorkingInAustriaView.as_view(), name='working_in_austria'),
    path(_('services/'), views.ServicesView.as_view(), name='services'),
    path(_('job-seeker-faqs/'), views.JobSeekerFaqView.as_view(), name='job_seeker_faqs'),
    # employer or company
    path(_('staffing-solutions/'), views.StaffingSolutionsView.as_view(), name='staffing_solutions'),
    path(_('submit-a-position/'), views.SubmitPositionView.as_view(), name='submit_a_position'),
    path(_('submit-a-position/thanks/'), views.SubmitPositionThanksView.as_view(), name='submit_a_position_thanks'),
    path(_('employer-faqs/'), views.EmployerFaqView.as_view(), name='employer_faqs'),
    path(_('employer-how-it-works/'), views.EmployerHowItWorksView.as_view(), name='employer_how_it_works'),
    path(_('portal/'), views.PortalView.as_view(), name='portal'),
    # both
    path(_('about/'), views.AboutView.as_view(), name='about'),
    path(_('contact/'), views.ContactView.as_view(), name='contact'),
    path(_('contact/thanks/'), views.ContactThanksView.as_view(), name='contact_thanks'),
    path(_('video-resume/'), views.VideoResumeView.as_view(), name='video_resume'),
    # other
    path(_('imprint/'), views.ImprintView.as_view(), name='imprint'),
    path(_('privacy/'), views.PrivacyView.as_view(), name='privacy'),
    path(_('agb/'), views.AgbView.as_view(), name='agb'),
]
