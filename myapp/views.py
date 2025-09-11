from django.shortcuts import render
from myapp.forms import NameForm,ContactForm
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index_view(request):
    return render (request, 'myapp/index.html')


def about_view(request):
     return render (request, 'myapp/about.html')


def contact_view(request):
      if request.method == 'POST':
           form = ContactForm(request.POST)
           if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'your ticket submited successfully')
           else:
                messages.add_message(request, messages.ERROR, 'your ticket didnt submited')
      form = ContactForm()              
      return render (request, 'myapp/contact.html', {'form':form})



def test(request):
      if request.method == 'POST':
           forms = ContactForm(request.POST)
           if forms.is_valid():
                forms.save()
                return HttpResponse('Done')
           else:
                return HttpResponse('NOT valid')
      forms = ContactForm()       
      return render (request, 'myapp/test.html', {"forms":forms})