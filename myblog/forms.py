from .models import Newspaper
from django import forms

class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = '__all__'