from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.calculator_index, name='calculator_index'),
]
