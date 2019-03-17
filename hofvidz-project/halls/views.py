from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Hall


# Create your views here.

class HallsTest(generic.TemplateView):
    template_name = 'halls_test.html'

class CreateHall(generic.CreateView):
    model = Hall
    fields = ['title']
    template_name = 'halls/create_hall.html'
    success_url = reverse_lazy('home')
