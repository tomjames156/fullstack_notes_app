from django.urls import path
from .views import *

urlpatterns = [
    path('', initial, name='initial'),
    path('notes/', get_notes, name='get_notes'),
    path('notes/<str:pk>/', get_note, name='get_note')
]
