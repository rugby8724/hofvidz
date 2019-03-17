from django.shortcuts import render, redirect
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

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateHall, self).form_valid(form)
        return redirect('home')


class DetailHall(generic.DetailView):
    model = Hall
    template_name = 'halls/detail_hall.html'
