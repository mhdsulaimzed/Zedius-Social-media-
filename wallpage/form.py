from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from wallpage.models import UserProfile,Post,Comment


class SignupForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]

class SigninForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=["profile_pic","bio","dob","city"]

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["caption","image"]
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["body"]

