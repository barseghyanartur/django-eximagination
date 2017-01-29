from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings

urlpatterns = [
    # Test templates for eximagination
    url(
        r'^$',
        TemplateView.as_view(template_name='eximagination/test.html'),
        name='eximagination.test'
    ),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
