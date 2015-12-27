# pylint: disable=bad-continuation

from cv.views import TheMainTemplateView, HashtagAjaxView, FeatureAjaxView, switch_ajax
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TheMainTemplateView.as_view(), name='mainpage'),
    url(r'^(?P<hashtag_id>[a-zA-Z]*)/?$', switch_ajax(HashtagAjaxView), 
        name='hashtag'),
    url(r'^(?P<hashtag_id>[a-zA-Z]*)/(?P<feature_id>[a-zA-Z]*)/?$',
        switch_ajax(FeatureAjaxView), name='feature')
)
