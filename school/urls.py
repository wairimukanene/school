from django.urls import path  
from school import views  

urlpatterns = [ 
    path('', views.school),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  