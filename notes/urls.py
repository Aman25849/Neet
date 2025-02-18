from django.urls import path
from . import views

urlpatterns = [
     path('neet/<str:user>', views.notes, name='notes')
]
