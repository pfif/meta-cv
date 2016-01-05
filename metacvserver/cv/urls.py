# pylint: disable=bad-continuation

from django.conf.urls import patterns, url
from cv.views import HashtagAjaxView, FeatureAjaxView
from themaintemplate.view import TheMainTemplateView, switch_ajax

urlpatterns = patterns('',
    url(r'^(?P<hashtag_id>[a-zA-Z]*)/?$', switch_ajax(HashtagAjaxView),
        name='hashtag'),
    url(r'^(?P<hashtag_id>[a-zA-Z]*)/(?P<feature_id>[a-zA-Z]*)/?$',
        switch_ajax(FeatureAjaxView), name='feature')
)
