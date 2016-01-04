# pylint: disable=bad-continuation

from django.conf.urls import patterns, url
from cv.views import TheMainTemplateView, HashtagAjaxView, FeatureAjaxView,\
                     switch_ajax

urlpatterns = patterns('',
    url(r'^$', TheMainTemplateView.as_view(), name='mainpage'),
    url(r'^(?P<hashtag_id>[a-zA-Z]*)/?$', switch_ajax(HashtagAjaxView),
        name='hashtag'),
    url(r'^(?P<hashtag_id>[a-zA-Z]*)/(?P<feature_id>[a-zA-Z]*)/?$',
        switch_ajax(FeatureAjaxView), name='feature')
)
