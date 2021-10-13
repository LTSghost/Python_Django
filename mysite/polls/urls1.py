from django.urls import path
from . import views

urlpatterns = [
    path('/321', views.TemIndex, name='TemIndex')
]