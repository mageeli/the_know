from  django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^posts/$', views.PostView.as_view(), name='posts'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post'),
    re_path(r'^addPost/$', views.WriteView.as_view(success_url="blog/posts/"), name='addPost')
]