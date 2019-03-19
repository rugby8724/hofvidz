from . models import Video
from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
        labels = {'url':'YouTube Video URL'}

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=257, label='Search for Videos')
