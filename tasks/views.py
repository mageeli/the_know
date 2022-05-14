from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import ToDoItem, ToDoList

class ListListView(ListView):
    model = ToDoList
    template_name = "tasks/tasks.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list_items"] = ToDoItem.objects.all()
        return context

class ItemListView(ListView):
    model = ToDoItem
    template_name = "tasks/tasks_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["pk"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["pk"])
        return context

class ListCreate(CreateView):
    model = ToDoList
    template_name = "tasks/add_task_list.html"
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context

class ItemCreate(CreateView):
    model = ToDoItem
    template_name = "tasks/add_task_item.html"
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
        "for_whom",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["pk"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["pk"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ItemUpdate(UpdateView):
    model = ToDoItem
    template_name = "tasks/add_task_item.html"
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
        "for_whom",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ListDelete(DeleteView):
    model = ToDoList
    template_name = "tasks/task_list_confirm_delete.html"
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")

class ItemDelete(DeleteView):
    model = ToDoItem
    template_name = "tasks/task_item_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context


