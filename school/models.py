from django.db import models

# Create your models here.

class Form1A(models.Model):
    # id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100,null=True, error_messages={'required': 'Enter a value for this name field.'})
    stream = models.CharField(max_length=100, null=True, error_messages={'required': 'Enter a value for this stream field.'})
    email = models.EmailField(null=True, error_messages={'required': 'Enter a value for this email field.'})
    contact = models.CharField(null=True, max_length=15, error_messages={'required': 'Enter a value for this contact field.'})

    def __str__(self):
        return "%s " %(self.name)
    class Meta:
        db_table = "school"





