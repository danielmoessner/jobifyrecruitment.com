from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.urls import path

sitemaps = {}

urlpatterns = [
    # sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # tinymce
    path('tinymce/', include('tinymce.urls')),
    # robots file
    path('robots.txt', TemplateView.as_view(template_name="general/robots.txt", content_type='text/plain')),
    # admin
    path('admin/', admin.site.urls),
    # error for testing
    path('error/', TemplateView.as_view(template_name='general/error.html'))
]

urlpatterns += i18n_patterns(
    path('', include('apps.frontend.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns += [path('__debug__/', include('debug_toolbar.urls')), ]
