from django.db import models
from django.contrib.auth.models import User
from positions.models import Position
from departments.models import Department


# Create your models here.


    

class Employee(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    employee_name=models.CharField(max_length=50)
    employee_email=models.CharField(max_length=50)
    employee_number=models.CharField(max_length=50)
    GENDER_CHOICE = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    ]
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICE,
        default="",
    )
    nationality=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    ID_CHOICE = [
        ('National_ID', 'National_ID'),
        ('Passport', 'Passport'),
        
    ]
    id_type=models.CharField(
        max_length=20,
        choices=ID_CHOICE,
        default="",
    )
    hire_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    SOCIAL_CHOICE = [
        ('Single', 'Single'),
        ('Maried', 'Maried'),
        
    ]
    social_status=models.CharField(
        max_length=20,
        choices=SOCIAL_CHOICE,
        default="",
    )
    date_birth=models.DateTimeField(auto_now=False, auto_now_add=False)
    blace_birth=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=50)
    idd=models.CharField(max_length=50)
    insured=models.BooleanField()
    is_active=models.BooleanField()
    has_medical=models.BooleanField()
    leaves_balance=models.CharField(max_length=50) 
    #contract=models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.employee_name



class Contract(models.Model):
    employee=models.ForeignKey(Employee,  related_name='employee' ,on_delete=models.CASCADE)
    Contract_CHOICE = [
        ('Casual', 'Casual'),
        ('trainee', 'trainee'),
        ('Contractors', 'Contractors'),
        
    ]
    contract_type=models.CharField(
        max_length=20,
        choices=Contract_CHOICE,
        default="",
    )
    contract_start=models.DateTimeField(auto_now_add=True)
    contract_end=models.DateTimeField(auto_now=False, auto_now_add=False)
    position=models.ForeignKey(Position, on_delete=models.CASCADE)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    manager=models.ForeignKey(Employee, related_name='manager' ,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.contract_type

