from django.shortcuts import render
from django.http import HttpResponse #needed to return
from django.views import View  #needed for class
# Create your views here.
def hello_world(request):
    return HttpResponse("hello world")


class hello_earth(View):
    def get(self, request):
        return HttpResponse("Hello Earth")
    
    
    
