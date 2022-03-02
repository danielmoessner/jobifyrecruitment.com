from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from apps.frontend import views
from django.urls import path

sitemaps = {

}

app_name = "frontend"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('initiative-application/', views.InitiativeApplicationView.as_view(), name='initiative_application'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="general/robots.txt", content_type='text/plain')),
]
