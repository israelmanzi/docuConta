from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TaskList(ListView):
    model = Task

class TaskView(DetailView):
    model = Task

class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'description', 'completed', 'date_created', 'date_completed']
    success_url = reverse_lazy('task_list')

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed', 'date_created', 'date_completed']
    success_url = reverse_lazy('task_list')

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')