from  django.urls import re_path, include
from questions.views import HomePageView, QuestionsView, QuestionDetailView, AddQuestionView

urlpatterns = [
    re_path(r'^$', HomePageView.as_view(), name='home'),
    re_path(r'^questions/$', QuestionsView.as_view(), name='questions'),
    re_path(r'^question/(?P<pk>[0-9]+)/$', QuestionDetailView.as_view(), name='question'),
    re_path(r'^addQuestion/$', AddQuestionView.as_view(success_url="/questions/"), name='addQuestion'),
    re_path('accounts/', include('django.contrib.auth.urls')),

              ]

