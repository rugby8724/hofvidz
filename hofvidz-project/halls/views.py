from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Hall, Video
from . forms import VideoForm, SearchForm
from django.http import Http404, JsonResponse
import urllib
import requests
from django.forms.utils import ErrorList
# alls us to create formsets
# from django.forms import formset_factory

YOUTUBE_API_KEY = 'AIzaSyDS5gLP-Ybf6Qry4tG3DaYXePdf5HwPAmw'
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
    hall = Hall.objects.get(pk=pk)

    if hall.user != request.user:
        raise Http404

    if request.method == 'POST':
        #Create
        form = VideoForm(request.POST)
        if form.is_valid():
            video = Video()
            video.hall = hall
            video.url = form.cleaned_data['url']
            parsed_url = urllib.parse.urlparse(video.url)
            video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
            if video_id:
                video.youtube_id = video_id[0]
                response = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id[0]}&key={YOUTUBE_API_KEY}')
                json = response.json()
                video.title = json['items'][0]['snippet']['title']
                video.save()
                return redirect('halls:detail_hall', pk)
            else:
                errors = form._errors.setdefault('url', ErrorList())
                errors.append('Needs to be a YouTube URL')

    return render(request, 'halls/add_video.html', {'form':form, 'search_form':search_form, 'hall':hall})

def video_search(request):
    return JsonResponse({'hello': 'yup'})
