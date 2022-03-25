from django import forms; 
from .models import Author, Publisher;

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'

class PublisherForm(forms.ModelForm):
    class Meta:
        model=Publisher
        fields='__all__'