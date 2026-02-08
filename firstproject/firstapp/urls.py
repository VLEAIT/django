from django.urls import path
from . import views

urlpattern = [
     path('function', views.hello_world),
     path('class', views.hello_earth.as_view()),
]