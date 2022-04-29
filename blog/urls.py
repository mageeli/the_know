from  django.urls import re_path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    re_path(r'^posts/$', login_required(views.PostView.as_view()), name='posts'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', login_required(views.PostDetailView.as_view()), name='post'),
    re_path(r'^addPost/$', login_required(views.WriteView.as_view(success_url="/blog/posts/")), name='addPost')
]