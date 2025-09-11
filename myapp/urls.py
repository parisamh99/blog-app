from django.urls import path
from .views import index_view,about_view,contact_view,test

app_name = 'myapp'

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('test/', test, name='test'),
]
