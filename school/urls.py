from django.urls import path
from school import views

urlpatterns = [
    path('', views.school, name='school'),
    path('show',views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('/update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.destroy),
]