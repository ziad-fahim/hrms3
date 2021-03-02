from django.db import models

# Create your models here.

class Department(models.Model):
    department_name=models.CharField(max_length=50)
    department_description=models.CharField(max_length=100)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.department_name

