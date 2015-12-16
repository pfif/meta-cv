# pylint: disable=bad-continuation

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cv.views.mainpage', name='mainpage'),
    url(r'^(?P<hashtag_id>[a-zA-Z]*)/?$', 'cv.views.hashtag', name='hashtag'),
    url(r'^(?P<hashtag_id>[a-zA-Z]*)/(?P<feature_id>[a-zA-Z]*)/?$',
        'cv.views.feature', name='feature')
)
