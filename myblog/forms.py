from .models import Newspaper,Comment
from django import forms

class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['post' ,'name', 'email', 'subject', 'message',]       