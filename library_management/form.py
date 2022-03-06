from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book


class Library_User(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','is_staff']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'