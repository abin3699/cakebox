from django import forms
from cakebxapp.models import User,Catagory,Cakes,Cake_variant,Offer
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2","phone","address"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model=Catagory
        fields=["types"]

class CakeAddForm(forms.ModelForm):
    class Meta:
        model=Cakes
        fields="__all__"


class CakeVarientForm(forms.ModelForm):
    class Meta:
        model=Cake_variant
        exclude=("cake",)


class CakeOfferForm(forms.ModelForm):
    class Meta:
        model=Offer
        exclude=("Cake_variant",)
        widgets={
            "start_date":forms.DateInput(attrs={"type":"date"}),
            "due_date":forms.DateInput(attrs={"type":"date"})
        }