from django import forms
from .models import Employee , Contract

class employeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user' , 'employee_name' , 'employee_email' , 'employee_number' , 'gender' , 'nationality' , 'address' , 'id_type' , 'hire_date' 
                    , 'social_status' , 'date_birth' , 'blace_birth' , 'Mobile' , 'idd' , 'insured' , 'is_active' , 
                    'has_medical' ]
    
class contractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['employee' , 'contract_type' ,  'contract_end' , 'position' , 'department' , 'manager' ]



class balanceForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name' ,  'leaves_balance' ]    


  