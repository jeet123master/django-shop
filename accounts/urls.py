from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Dashboard, name="dashboard"),
    path('user-register/', views.UserRegister, name="register"),
    path('user-login/', views.UserLogin, name="login"),
    path('user-logout/', views.UserLogout, name="logout"),


]
