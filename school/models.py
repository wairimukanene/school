from django.db import models

# Create your models here.

class Form1A(models.Model):  
    id = models.CharField(max_length=20, primary_key=True)  
    name = models.CharField(max_length=100)  
    stream = models.CharField(max_length=100)
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 

    def __str__(self):
        return "%s " %(self.name) 
    class Meta:  
        db_table = "school"  





