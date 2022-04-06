from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserProfileForm(forms.ModelForm):
    gender_choices =(
        ('MALE','MALE'),
        ('FEMALE','FEMALE')
    )
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    Date_of_Birth = forms.DateField( widget=forms.DateInput)
    class Meta:
        model = UserProfile
        fields = '__all__'