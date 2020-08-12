from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import blog

class AddPostForm(ModelForm):
    class Meta:
        model = blog
        fields = [
            "image",
            "heading",
            "brief",
            "author",
        ]

class user_form(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]