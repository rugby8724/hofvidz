from django.urls import path
# Imports Djangos Login and Logout Views, no need to create in views.py
from django.contrib.auth import views as auth_views
from . import views

# if we want to use in our html templates we can use the accounts name
app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
