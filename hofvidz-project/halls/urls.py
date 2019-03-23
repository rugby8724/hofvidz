#halls
from django.urls import path
from . import views

app_name = 'halls'

urlpatterns = [
    path('create/', views.CreateHall.as_view(), name='create_hall'),
    path('<int:pk>/', views.DetailHall.as_view(), name='detail_hall'),
    path('update/<int:pk>/', views.UpdateHall.as_view(), name='update_hall'),
    path('delete/<int:pk>/', views.DeleteHall.as_view(), name='delete_hall'),
    path('addvideo/<int:pk>/', views.add_video, name='add_video'),
    path('addvideo/<int:pk>/video/search/', views.video_search, name='video_search'),
    path('video/delete/<int:pk>/', views.DeleteVideo.as_view(), name='delete_video'),
]
