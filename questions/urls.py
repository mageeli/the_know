from  django.urls import re_path, include
from questions.views import HomePageView, QuestionsView, QuestionDetailView, AddQuestionView,EditQuestionView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    re_path(r'^$', HomePageView, name='home'),
    re_path(r'^questions/$', login_required(QuestionsView.as_view()), name='questions'),
    re_path(r'^question/(?P<pk>[0-9]+)/$', login_required(QuestionDetailView.as_view()), name='question'),
    re_path(r'^question/(?P<pk>[0-9]+)/edit/$', login_required(EditQuestionView.as_view()), name='editQuestion'),
    re_path(r'^addQuestion/$', login_required(AddQuestionView.as_view(success_url="/questions/")), name='addQuestion'),
    re_path('accounts/', include('django.contrib.auth.urls')),

              ]

