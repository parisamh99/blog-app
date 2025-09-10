from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index_view(request):
    return render (request, 'myapp/index.html')


def about_view(request):
     return render (request, 'myapp/about.html')


def contact_view(request):
      return render (request, 'myapp/contact.html')