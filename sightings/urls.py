from django.urls import path
from . import views

urlpatterns =[
    path('sightings/', views.index, name='index'),
]