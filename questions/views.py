from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
import textwrap
from django.views.generic import TemplateView
from .models import Question



class QuestionsView(ListView):
    template_name = "question/questions.html"
    model = Question

class QuestionDetailView(DetailView):
    template_name = "question/question.html"
    model = Question


class AddQuestionView(CreateView):
    template_name = 'question/add_question.html'
    model = Question
    fields = ['title', 'body']

    def get_initial(self,):
        initial = super().get_initial()
        return initial


def HomePageView(request):
    return render(request, 'index.html')


