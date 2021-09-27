from django.forms import ModelForm
from django import forms

from reporting.models import MyUser,Course,Batch,Timesheet

from reporting.admin import UserCreationForm

class AddUserForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = MyUser
        fields = ["email", "role", "password1", "password2"]
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-select"})
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

class SigninForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class TimesheetForm(forms.ModelForm):
    class Meta:
        model = Timesheet
        fields=["batch","topic","topic_status"]

        widgets={
            "batch":forms.Select(attrs={"class":"form-control"}),
            "topic":forms.TextInput(attrs={"class":"form-control"}),
            "topic_status":forms.Select(attrs={"class":"form-control"})
        }

