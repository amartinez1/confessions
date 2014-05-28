from django.conf.urls import patterns, include, url
from .views import PostListView,ConfessForm





urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'confesionsapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^list/$',PostListView.as_view(), name = 'list'),
    url(r'^form/$',ConfessForm.as_view(),name='form')

)
