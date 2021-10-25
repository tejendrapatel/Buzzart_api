from django.urls import path
from .import views

urlpatterns = [
    path('', views.HOME, name='home'),
    path('user/', views.USERRAN, name='home'),
]