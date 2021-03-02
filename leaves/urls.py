from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", views.Leaves, name="Leave_master"),
    
    path("add/", views.add_leave, name="add_leave"),
    path("create/", views.create_leave, name="create_leave"),
    path("all/", views.All_Leavess, name="all_leaves"),
    path("tax/", views.compare, name="tax"),
    path("employee_leaves/", views.emp_leaves, name="leaves"),
    path("dashboard/", views.Display_Dashboard, name="Dashboard"),
     path("show/<pk>", views.display_leave_details, name="show"),
    path("accept/<pk>", views.Accept, name="accept"),
    path("reject/<pk>", views.Reject, name="reject"),
]