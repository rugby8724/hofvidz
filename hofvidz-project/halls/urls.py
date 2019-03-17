#halls
from django.urls import path
from . import views

app_name = 'halls'

urlpatterns = [
    path('create/', views.CreateHall.as_view(), name='create_hall'),
]
