from django import forms
from .models import Leave_Master , All_Leaves
from django.db.models.signals import pre_save
from employees.models import Employee

class LeavesForm(forms.ModelForm):
     class Meta:
        model = Leave_Master
        fields = ['leave_type' , 'leave_value']


class AllLeavesForm(forms.ModelForm):
      class Meta:
         model = All_Leaves
         fields = ['employee' , 'leave_type' , 'leave_start' , 'leave_end' , 'resume_date' , 'leave_reason']

      def clean(self):
         cleaned_data = super().clean()
         leave_start = cleaned_data.get("leave_start")
         leave_end = cleaned_data.get("leave_end")
         resume_date = cleaned_data.get("resume_date")
         if leave_end < leave_start:
            raise forms.ValidationError("End date should be greater than start date.") 
         if resume_date < leave_end:
            raise forms.ValidationError("Resume date should be greater than end date.")   




class Login(forms.ModelForm):
    class Meta: 
       fields = ['user' ,  'password' ]
      




      
      