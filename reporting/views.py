import django_filters
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django_filters.views import FilterView
from reporting.decorators import Sign_required
from django.utils.decorators import method_decorator
from reporting import forms
from reporting.models import MyUser,Course,Batch,Timesheet
from reporting.filters import TimesheetFilter
from django.contrib import messages

class SignInView(TemplateView):
    template_name = "reporting/user_login.html"
    form_class=forms.SigninForm

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["form"]=self.form_class()
        return context

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                if request.user.is_admin:
                    return redirect("adminhome")
                else:
                    return redirect("userhome")
            else:
                messages.error(request, "please enter correct username/password")
                return redirect('signin')


class SignOut(TemplateView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("signin")

@method_decorator(Sign_required,name='dispatch')
class UserHome(TemplateView):
    template_name = "reporting/user_home.html"

# @method_decorator(admin_permission_required,name='dispatch')
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
# @method_decorator(admin_permission_required,name='dispatch')
class Userlist(ListView):
    model = MyUser
    template_name = "reporting/user_list.html"
    context_object_name = "users"

# @method_decorator(admin_permission_required,name='dispatch')
class UserEdititems(UpdateView):
    model = MyUser
    template_name = "reporting/user_change.html"
    form_class = forms.AddUserForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("adduser")

# @method_decorator(admin_permission_required,name='dispatch')
class UserDetailView(DetailView):
    model = MyUser
    template_name = "reporting/userdetailview.html"
    context_object_name = "users"

@method_decorator(Sign_required,name='dispatch')
class AddTimeSheetView(CreateView):
    model = Timesheet
    form_class=forms.TimesheetForm
    template_name = "reporting/add_timesheet.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["timesheets"]=self.model.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            timesheet=form.save(commit=False)
            timesheet.user=request.user
            timesheet.save()
            return redirect("addtimesheet")

@method_decorator(Sign_required,name='dispatch')
class UserTimesheetsList(FilterView):
    model = Timesheet
    template_name = "reporting/user_timesheet_list.html"
    context_object_name = "timesheets"
    filterset_class=TimesheetFilter
    context={}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filters"] = self.filterset_class
        # if self.request.user.is_admin:
        #     queryset = self.model.objects.all()
        # else:
        #     queryset = self.model.objects.filter(user=self.request.user,verified=False)
        # context["queryset"]=queryset
        return context
    # def get(self,request, *args, **kwargs):
    #     filters = TimesheetFilter(request.GET, queryset=Timesheet.objects.all())
    #     return render(request,self.template_name , {"filters": filters})
    # def get(self, request, *args, **kwargs):
    #     self.context["filters"]=self.filter_set
    #
    #     return render(request, self.template_name, self.context)

    #
    def get_queryset(self):
        if self.request.user.is_admin:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(user=self.request.user, verified=False)
        return queryset

# @method_decorator(admin_permission_required,name='dispatch')
class AdminTimesheetsList(FilterView):
    model = Timesheet
    template_name = "reporting/admin_timesheets_list.html"
    context_object_name = "timesheets"
    filterset_class=TimesheetFilter
    context={}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filters"] = self.filterset_class
        if self.request.user.is_admin:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(user=self.request.user, verified=False)
        context["queryset"]=queryset
        return context

class ChangeUserTimesheetsList(UpdateView):
    model = Timesheet
    template_name = "reporting/user_timesheet_change.html"
    form_class = forms.TimesheetForm
    success_url = reverse_lazy("usertimesheetlist")

#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
#admin side

# @method_decorator(admin_permission_required,name='dispatch')
class AdminHome(TemplateView):
    template_name = "reporting/adminhome.html"
    # def get(self,request,*args,**kwargs):
    #     return render(request,"reporting/adminhome.html")

# @method_decorator(admin_permission_required,name='dispatch')
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
# @method_decorator(admin_permission_required,name='dispatch')
class Courselistview(ListView):
    model=Course
    template_name = "reporting/course_list.html"

# @method_decorator(admin_permission_required,name='dispatch')
class CourseDetailView(DetailView):
    model=Course
    template_name = "reporting/CoursedetailView.html"
    pk_url_kwarg = "id"
    context_object_name = "course"

# @method_decorator(admin_permission_required,name='dispatch')
class EditCourseChange(UpdateView):
    model = Course
    template_name = "reporting/course_change.html"
    form_class=forms.CourseAddForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("course")

# @method_decorator(admin_permission_required,name='dispatch')
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

# @method_decorator(admin_permission_required,name='dispatch')
class BatchListView(ListView):
    model = Batch
    template_name = "reporting/batch_list.html"
    context_object_name = "batches"

# @method_decorator(admin_permission_required,name='dispatch')
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

# @method_decorator(admin_permission_required,name='dispatch')
class BatchDetailView(DetailView):
    model = Batch
    template_name = "reporting/batchdetailview.html"
    context_object_name = "batch"

# @method_decorator(admin_permission_required,name='dispatch')
class TimesheetVerification(TemplateView):
    model = Timesheet
    pk_url_kwarg="id"
    def get(self, request, *args, **kwargs):
        timesheet=self.model.objects.get(id=kwargs["id"])
        timesheet.verified=True
        timesheet.save()
        return redirect("usertimesheetlist")


# class TimesheetFiltersView(TemplateView):
#     model= Timesheet
#     template_name = "reporting/user_timesheet_list.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["filters"] = django_filters.TimesheetFilter
#         return context







