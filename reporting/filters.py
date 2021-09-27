import django_filters
from reporting.models import Timesheet,MyUser,Batch
from django import forms


class TimesheetFilter(django_filters.FilterSet):
    user= django_filters.ModelChoiceFilter(queryset=MyUser.objects.all(),
                                           widget=forms.Select(attrs={"class":"form-select"}))
    batch = django_filters.ModelChoiceFilter(queryset=Batch.objects.all(), widget =forms.Select(attrs={"class": "form-select"}))

    date=django_filters.DateFilter(widget=forms.DateInput(attrs={"type":"date"}))

    class Meta:
        model = Timesheet
        fields=["user","batch","date"]