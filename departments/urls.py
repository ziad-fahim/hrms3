from django.urls import path
from . import views


urlpatterns = [
    path("", views.departments, name="all_departments"),
    path("add/", views.create_department, name="create-department"),
]
