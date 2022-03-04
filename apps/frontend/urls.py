from django.utils.translation import gettext_lazy as _
from apps.frontend import views
from django.urls import path

app_name = "frontend"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(_('initiative-application/'), views.InitiativeApplicationView.as_view(), name='initiative_application'),
    path(_('for-companies/'), views.ForCompaniesView.as_view(), name='for_companies'),
    path(_('for-applicants/'), views.ForApplicantsView.as_view(), name='for_applicants'),
    path(_('portal/'), views.PortalView.as_view(), name='portal'),
    path(_('contact/'), views.ContactView.as_view(), name='contact'),
    path(_('imprint/'), views.ImprintView.as_view(), name='imprint'),
    path(_('privacy/'), views.PrivacyView.as_view(), name='privacy'),
]
