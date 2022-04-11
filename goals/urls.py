from  django.urls import re_path, include

from . import views

urlpatterns = [
    re_path(r'^$', views.goals_list_view, name='goal_list'),
    re_path(r'^(?P<goal_pk>\d+)/$', views.goal_detail_view, name='goal_detail'),
    re_path(r'^category/(?P<category_pk>\d+)/$', views.goals_list_view, name='category'),
    re_path(r'^new/$', views.new_goal_view, name='new_goal'),
    re_path(r'^category/new/$', views.new_category_view, name='new_category'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.edit_goal_view, name='edit_goal'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.delete_goal_view, name='delete_goal'),
    re_path(r'^(?P<pk>\d+)/goal-achieved/$', views.goal_achieved_view, name='goal_achieved'),
    re_path(r'^(?P<goal_pk>\d+)/actions/new/$', views.new_action_view, name='new_action'),
    re_path(r'^(?P<goal_pk>\d+)/actions/(?P<action_pk>\d+)$', views.manage_action_view, name='manage_action'),
    re_path(r'^(?P<goal_pk>\d+)/actions/(?P<action_pk>\d+)/delete/$', views.delete_action_view, name='delete_action'),
    re_path(r'^(?P<goal_pk>\d+)/action-log-list/$', views.action_log_list_view, name='action_log_list'),
    re_path(r'^(?P<goal_pk>\d+)/action-log/$', views.action_log_view, name='action_log'),
    re_path(
        r'^(?P<goal_pk>\d+)/action-log/(?P<action_log_pk>\d+)/delete/$',
        views.delete_action_log_view,
        name='delete_action_log'
    ),
]
