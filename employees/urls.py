from django.urls import path
from . import views


urlpatterns = [
    path("", views.employees, name="all_employees"),
    path("add/", views.create_employee, name="create_employee"),
    path("update/<pk>", views.update_employee, name="update_employee"),

    path("add_balance/<pk>", views.add_balance, name="add_balance"),

    
    path("delete/<pk>", views.delete_employee, name="delete_employee"),
    path("contracts/", views.contracts, name="all_contracts"),
    path("create_contract/", views.create_contract, name="create_contract"),
    path("balance/", views.employee_balance, name="employee_balance"),
    
]