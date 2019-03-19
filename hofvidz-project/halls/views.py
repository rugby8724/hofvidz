from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Hall, Video
from . forms import VideoForm, SearchForm
# alls us to create formsets
# from django.forms import formset_factory


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
        return redirect('dashboard')


class DetailHall(generic.DetailView):
    model = Hall
    template_name = 'halls/detail_hall.html'

class UpdateHall(generic.UpdateView):
    model = Hall
    template_name = 'halls/update_hall.html'
    # fields user is allowed to update
    fields = ['title']
    success_url = reverse_lazy('dashboard')

class DeleteHall(generic.DeleteView):
    model = Hall
    template_name = 'halls/delete_hall.html'
    success_url = reverse_lazy('dashboard')

def add_video(request, pk):
    # VideoFormSet = formset_factory(VideoForm, extra=5)
    form = VideoForm()
    search_form = SearchForm()

    if request.method == 'POST':
        #Create
        filled_form = VideoForm(request.POST)
        if filled_form.is_valid():
            video = Video()
            video.url = filled_form.cleaned_data['url']
            video.title = filled_form.cleaned_data['title']
            video.youtube_id = filled_form.cleaned_data['youtube_id']
            video.hall = Hall.objects.get(pk=pk)
            video.save()

    return render(request, 'halls/add_video.html', {'form':form, 'search_form':search_form})
