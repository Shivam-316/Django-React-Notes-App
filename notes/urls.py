from unicodedata import name
from django.urls import path
from .views import ListNoteApiView, CreateNoteApiView, DetailNoteApiView

urlpatterns = [
    path('create/', CreateNoteApiView.as_view(), name = 'create_note'),
    path('<int:pk>/', DetailNoteApiView.as_view(), name = 'deatil_note'),
    path('', ListNoteApiView.as_view(), name='list_notes'),
]