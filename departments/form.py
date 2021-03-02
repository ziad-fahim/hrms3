from django import forms
from .models import Department

class departmentForm(forms.ModelForm):
    
    class Meta:
        model = Department
        fields = ['department_name' , 'department_description'  , 'end_date']

 
    
