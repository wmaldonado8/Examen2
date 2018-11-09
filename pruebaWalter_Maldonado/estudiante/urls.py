from django.urls import path
from . import views

urlpatterns = [
    path('', views.Principal, name ='estudiante'),
    path('crear/', views.crear, name ='crear'),
    ]
