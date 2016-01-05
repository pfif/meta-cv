# pylint: disable=bad-continuation

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from themaintemplate.view import TheMainTemplateView

from cv import urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TheMainTemplateView.as_view(), name='mainpage'),
    url(r'^', include(urls))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
