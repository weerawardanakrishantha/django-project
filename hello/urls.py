from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.index, name='index'),
    path('brian', views.brian, name='brian'),
]
