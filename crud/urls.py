from django.urls import path
from . import views

urlpatterns = [

#path('', views.index, name= 'index'),
path('', views.addandshow, name= 'addandshow'),
path('update_student/<int:id>/', views.update_student, name= 'update_student'),
path('delete_student/<int:id>/', views.delete_student, name= 'delete_student'),
]
