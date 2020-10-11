from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Name")
    email = forms.EmailField()
    age = forms.IntegerField(label="AGE")
    gender = forms.CharField(max_length=6, label="Gender",
                             widget=forms.TextInput(attrs={'placeholder': 'Male | Female'}))

    class Meta:
        model = User
        fields = ["username", "age", "gender", "email", ]


class LogInForm(AuthenticationForm):
    username = forms.CharField()

    class Meta:
        fields = ["username", "password"]
