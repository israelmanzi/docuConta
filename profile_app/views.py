from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from profile_app.models import Profile

class ProfileList(ListView):
    model = Profile
    paginate_by = 5

class ProfileView(DetailView):
    model = Profile

class ProfileCreate(CreateView):
    model = Profile
    fields = ['username', 'firstName', 'lastName', 'email', 'profilePicture', 'role']
    success_url = reverse_lazy('profile_list')

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['username', 'firstName', 'lastName', 'email', 'profilePicture', 'role']
    success_url = reverse_lazy('profile_list')

class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('profile_list')