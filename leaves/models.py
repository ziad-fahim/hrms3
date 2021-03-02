from django.db import models
from employees.models import Employee
from datetime import date
# Create your models here.

STATUS_CHOICE = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Waiting to approve', 'Waiting to approve'),
        
    ]

LEAVE_CHOICE = [
        ('Casual', 'Casual'),
        ('Annual', 'Annual'),
        ('Sick', 'Sick')
  
    ]

class Leave_Master(models.Model):
    leave_type=models.CharField(max_length=50)
    leave_value=models.CharField(max_length=2)
    def __str__(self):
        return self.leave_type

class Taxes(models.Model):
    percent =  models.FloatField()
    start_range = models.IntegerField()
    end_range =  models.IntegerField(null=True)
    difference = models.IntegerField(null=True)
    tax = models.IntegerField(null=True)

class All_Leaves(models.Model):
    employee=models.ForeignKey(Employee, related_name='temp', on_delete=models.CASCADE, null=True)
    leave_type=models.ForeignKey(Leave_Master, on_delete=models.CASCADE, null=True)
    leave_start=models.DateField(auto_now=False, auto_now_add=False)
    leave_end=models.DateField(auto_now=False, auto_now_add=False)
    #number_of_days=models.CharField(max_length=2)
    resume_date=models.DateField(auto_now=False, auto_now_add=False)
    leave_reason=models.CharField(max_length=200)
    Status=models.CharField(
        max_length=20,
        default="WAITING FOR APPROVE",
    )
    
    #def __str__(self):
        #return self.leave_type

    