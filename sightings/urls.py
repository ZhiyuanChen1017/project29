from django.urls import path
from . import views

urlpatterns =[
    path('sightings/', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/add/', views.add, name='add'),
    path('sightings/<str:unique_squirrel_id>/', views.edit_squirrel, name='edit'),
]
