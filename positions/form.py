from django import forms
from .models import Position

class positionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['position_name' , 'position_description' , 'end_date']