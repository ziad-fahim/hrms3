from django.db import models
# Create your models here.
class Position(models.Model):
    position_name=models.CharField(max_length=50)
    position_description= models.CharField(max_length=100)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.position_name
    
   
    