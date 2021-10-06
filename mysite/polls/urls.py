from django.urls import path
from . import views

urlpatterns = [
    path('polls_Sec',views.index, name='index'),
]