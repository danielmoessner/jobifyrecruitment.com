from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.urls import path

urlpatterns = [
    # frontend
    path('', include('apps.frontend.urls')),
    # admin
    path('admin/', admin.site.urls),
    # error for testing
    path('error/', TemplateView.as_view(template_name='general/error.html'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns += [path('__debug__/', include('debug_toolbar.urls')), ]
