from django.views.generic import TemplateView
from halls.models import Hall, Video

class HomePage(TemplateView):
    model = Hall
    rencent_halls = model.objects.all().order_by('-id')[:3]
    popular_halls = [model.objects.get(pk=2),model.objects.get(pk=7),model.objects.get(pk=5)]
    template_name = 'index.html'
