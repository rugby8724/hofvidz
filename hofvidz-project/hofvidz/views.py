from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class Dashboard(TemplateView):
    template_name = 'dashboard.html'
