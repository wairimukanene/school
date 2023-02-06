from django import forms  
from school.models import Form1A
from django.forms import fields

class Form1AForm(forms.ModelForm):  
    class Meta:  
        model = Form1A  
        fields = "__all__"  

