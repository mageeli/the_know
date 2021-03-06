from django.shortcuts import render
from django.views import generic
from .models import Post
from django.shortcuts import redirect, reverse

# Create your views here.
class PostView(generic.ListView):
    template_name = 'blog/posts.html'
    model = Post

class PostDetailView(generic.DetailView):
    template_name = "blog/post.html"
    model = Post


class WriteView(generic.CreateView):
    template_name = 'blog/post_new.html'
    model = Post
    fields = ['title', 'text']

    def get_initial(self,):
        initial = super().get_initial()
        return initial

class UpdateView(generic.UpdateView):
    template_name = 'blog/post_edit.html'
    model = Post
    fields = ['title', 'text']

    def get_success_url(self):
        return reverse('post', kwargs={
            'pk': self.object.pk,
        })
