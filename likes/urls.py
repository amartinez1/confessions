from django.conf.urls import patterns, include, url
from .views import retrieve_token,like,unlike,like_count,fill_modal





urlpatterns = patterns('',

    url(r'^getCookie/$',retrieve_token, name = 'token'),
    url(r'^like/$',like.as_view(),name='like'),
    url(r'^unlike/$',unlike,name='unlike'),
    url(r'^like_count/$',like_count,name='like_count'),
    url(r'^fill/$',fill_modal.as_view(),name='fill'),


    # (?P<id>\d+)/

)
