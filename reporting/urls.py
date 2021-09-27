from django.urls import path
from reporting import views
urlpatterns=[
    path("home",views.AdminHome.as_view(),name="adminhome"),
    path("users/add",views.AddUser.as_view(),name="adduser"),
    path("course",views.CourseAdd.as_view(),name="course"),
    path("batch",views.BatchAdd.as_view(),name="batch"),
    path("courselist",views.Courselistview.as_view(),name="courselist"),
    path("batchlist",views.BatchListView.as_view(),name="batchlist"),
    path("batchchange/<int:id>",views.EditBatchItems.as_view(),name="batchchange"),
    path("coursechange/<int:id>",views.EditCourseChange.as_view(),name="coursechange"),
    path("userlist",views.Userlist.as_view(),name="userlist"),
    path("userchange/<int:id>",views.UserEdititems.as_view(),name="userchange"),
    path("course/details/<int:id>",views.CourseDetailView.as_view(),name="coursedetails"),
    path("batch/detail/<pk>",views.BatchDetailView.as_view(),name="batchdetails"),
    path("users/detail/<pk>",views.UserDetailView.as_view(),name="userdetails"),
    path("accounts/login",views.SignInView.as_view(),name="signin"),
    path("users/home",views.UserHome.as_view(),name="userhome"),
    path("accounts/logout", views.SignOut.as_view(), name="signout"),
    path("users/addtimesheet",views.AddTimeSheetView.as_view(),name="addtimesheet"),
    path("users/timesheetlistview",views.UserTimesheetsList.as_view(),name="usertimesheetlist"),
    path("admin/timesheet/listview",views.AdminTimesheetsList.as_view(),name="adminlistview"),
    path("users/timesheet/change/<pk>",views.ChangeUserTimesheetsList.as_view(),name="changeusertimesheet"),
    path("head/timesheet/verification/<int:id>",views.TimesheetVerification.as_view(),name="timesheetverification")
]