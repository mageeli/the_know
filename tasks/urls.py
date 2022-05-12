from  django.urls import re_path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    re_path(r'', login_required(views.ListListView.as_view()), name='index'),
    re_path(r'list/<int:list_id>/',views.ItemListView.as_view(), name="list"),
    re_path("list/add/", views.ListCreate.as_view(), name="list-add"),
    # CRUD patterns for ToDoItems
    re_path("list/<int:list_id>/item/add/",views.ItemCreate.as_view(),name="item-add",),
    re_path("list/<int:list_id>/item/<int:pk>/",views.ItemUpdate.as_view(), name="item-update",),
    re_path("list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"),
    re_path("list/<int:list_id>/item/<int:pk>/delete/",views.ItemDelete.as_view(),name="item-delete",),
]