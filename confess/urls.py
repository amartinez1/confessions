from django.conf.urls import patterns, include, url
from .views import PostListView,ConfessForm,PostDetailView,postList,newList,popularList





urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'confesionsapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',PostListView.as_view(), name = 'list'),
    url(r'^list/$',PostListView.as_view()),
    url(r'^confessions/$',postList,name = 'list'),
    url(r'^form/$',ConfessForm.as_view(),name='form'),
    url(r"^confessions/(?P<slug>[^\.]+)/$", PostDetailView.as_view(), name = 'detail'),
    url(r'^new/$',newList,name='new'),
    url(r'^popular/$',popularList,name='popular'),

)
