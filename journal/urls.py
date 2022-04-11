from  django.urls import re_path, include

from . import views

urlpatterns = [
    re_path(r'^journal/$', views.goal_journal_view, name='goal_journal'),
    re_path(r'^goals/(?P<goal_pk>\d+)/entries/new/$', views.new_entry_view, name='new_entry'),
    re_path(r'^entries/(?P<entry_pk>\d+)/edit/$', views.edit_entry_view, name='edit_entry'),
    re_path(r'^entries/(?P<entry_pk>\d+)/delete/$', views.delete_entry_view, name='delete_entry'),
]
