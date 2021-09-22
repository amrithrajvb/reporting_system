from django.forms import ModelForm
from django import forms

from reporting.models import MyUser,Course,Batch

from reporting.admin import UserCreationForm

class AddUserForm(UserCreationForm):
    model=MyUser
    fields=["email","role","password1","password2"]
    widgets={
        "email":forms.EmailInput(attrs={"class":"form-control"}),
        "role":forms.Select(attrs={"class":"form-select"}),
        "password1": forms.PasswordInput(attrs={"class": "form-control"}),
        "password2": forms.TextInput(attrs={"class": "form-control"})
    }

class CourseAddForm(ModelForm):
    class Meta:
        model = Course
        fields = ["course_name"]
        widgets = {
            "course_name": forms.TextInput(attrs={"class": "form-control"}),

        }

class BatchAddForm(ModelForm):
    class Meta:
        model=Batch
        fields=["course","batch_name"]
        widgets={
            "course":forms.Select(attrs={"class":"form-select"}),
            "batch_name":forms.TextInput(attrs={"class":"form-control"}),

        }

