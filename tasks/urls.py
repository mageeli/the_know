from  django.urls import re_path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    re_path(r'^lists/$', login_required(views.ListListView.as_view()), name='index'),
    re_path(r'^list/(?P<pk>[0-9]+)/$', login_required(views.ItemListView.as_view()), name='list'),
    re_path(r'^list/(?P<pk>[0-9]+)/delete/$', login_required(views.ListDelete.as_view()), name='list-delete'),
    re_path(r'^lists/add/$', login_required(views.ListCreate.as_view(success_url="/tasks/lists/")), name='list-add'),
    re_path(r'^list/(?P<pk>[0-9]+)/item/add/$', login_required(views.ItemCreate.as_view()), name='item-add'),
    re_path(r'^list/(?P<list_id>[0-9]+)/item/(?P<pk>[0-9]+)/delete/$', login_required(views.ItemDelete.as_view()), name='item-delete'),

    # re_path(r'^post/(?P<pk>[0-9]+)/$', login_required(views.PostDetailView.as_view()), name='post'),
    re_path(r'^list/(?P<list_id>[0-9]+)/item/(?P<pk>[0-9]+)/update$', login_required(views.ItemUpdate.as_view()), name='item-update'),

]
# urlpatterns = [
#     re_path(r'', login_required(views.ListListView.as_view()), name='index'),
#     re_path(r'list/<int:list_id>/',views.ItemListView.as_view(), name="list"),
#     re_path(r'^posts/$', login_required(views.PostView.as_view()), name='posts'),
#     re_path("list/add/", views.ListCreate.as_view(), name="list-add"),
#     # CRUD patterns for ToDoItems
#     re_path("list/<int:list_id>/item/add/",views.ItemCreate.as_view(),name="item-add",),
#     re_path("list/<int:list_id>/item/<int:pk>/",views.ItemUpdate.as_view(), name="item-update",),
#     re_path("list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"),
#     re_path("list/<int:list_id>/item/<int:pk>/delete/",views.ItemDelete.as_view(),name="item-delete",),
# ]