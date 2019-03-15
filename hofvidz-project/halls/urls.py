#halls
from django.urls import path
from . import views

app_name = 'halloffame'

urlpatterns = [
    path('create/', views.create_hall, name='create_hall'),
]
