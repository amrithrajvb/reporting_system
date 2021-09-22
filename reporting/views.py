from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView
# Create your views here.

from reporting import forms
from reporting.models import MyUser,Course,Batch

class AdminHome(TemplateView):
    template_name = "reporting/adminhome.html"
    # def get(self,request,*args,**kwargs):
    #     return render(request,"reporting/adminhome.html")


class AddUser(CreateView):
    model=MyUser
    form_class=forms.AddUserForm
    template_name = "reporting/user_add.html"
    success_url = reverse_lazy("adduser")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["users"]=self.model.objects.all()
        return context
    # context={}
    # def get(self, request, *args, **kwargs):
    #     form=self.form_class()
    #     self.context["form"]=form
    #     return render(request,self.template_name,self.context)
    # def post(self, request, *args, **kwargs):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("adminhome")

class Userlist(ListView):
    model = MyUser
    template_name = "reporting/user_list.html"
    context_object_name = "users"

class UserEdititems(UpdateView):
    model = MyUser
    template_name = "reporting/user_change.html"
    form_class = forms.AddUserForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("adduser")

class UserDetailView(DetailView):
    model = MyUser
    template_name = "reporting/userdetailview.html"
    context_object_name = "users"


class CourseAdd(CreateView):
    model=Course
    form_class=forms.CourseAddForm
    template_name = "reporting/CourseAdd.html"
    success_url = reverse_lazy("course")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["courses"]=self.model.objects.all()
        return context

    # context={}
    # def get(self, request, *args, **kwargs):
    #     form=self.form_class()
    #     self.context["form"]=form
    #     return render(request,self.template_name,self.context)
    # def post(self, request, *args, **kwargs):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("adminhome")
class Courselistview(ListView):
    model=Course
    template_name = "reporting/course_list.html"

class CourseDetailView(DetailView):
    model=Course
    template_name = "reporting/CoursedetailView.html"
    pk_url_kwarg = "id"
    context_object_name = "course"

class EditCourseChange(UpdateView):
    model = Course
    template_name = "reporting/course_change.html"
    form_class=forms.CourseAddForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("course")


class BatchAdd(CreateView):
    model = Batch
    form_class = forms.BatchAddForm
    template_name = "reporting/batch_list.html"
    success_url = reverse_lazy("batch")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["batch"]=self.model.objects.all()
        return context
    # context = {}
    #
    # def get(self, request, *args, **kwargs):
    #     form = self.form_class()
    #     self.context["form"] = form
    #     return render(request, self.template_name, self.context)
    # def post(self, request,*args,**kwargs):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("adminhome")


    # context={}
    # def get(self, request, *args, **kwargs):
    #     courses=self.model.objects.all()
    #     self.context["courses"]=courses
    #     return render(request,self.template_name,self.context)

class BatchListView(ListView):
    model = Batch
    template_name = "reporting/batch_list.html"
    context_object_name = "batches"

class EditBatchItems(UpdateView):
    model=Batch
    template_name = "reporting/batch_change.html"
    form_class=forms.BatchAddForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("batch")
    # context={}
    #
    # def get(self,request,*args,**kwargs):
    #     batch_id=kwargs["id"]
    #     batches=self.model.objects.get(id=batch_id)
    #     form=self.form_class(instance=batches)
    #     self.context["form"]=form
    #     return render(request,self.template_name,self.context)
    #
    # def post(self,request,*args,**kwargs):
    #     batch_id=kwargs["id"]
    #     batches=self.model.objects.get(id=batch_id)
    #     form=self.form_class(request.POST,instance=batches)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("batchlist")


class BatchDetailView(DetailView):
    model = Batch
    template_name = "reporting/batchdetailview.html"
    context_object_name = "batch"




