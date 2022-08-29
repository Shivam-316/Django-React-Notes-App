from django.shortcuts import render
from .serializer import NoteSerializer
from .models import Note
from rest_framework import generics
# Create your views here.

class ListNoteApiView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(author = self.request.user)


class CreateNoteApiView(generics.CreateAPIView):
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        return serializer.save(author = self.request.user)

class DetailNoteApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return Note.objects.filter(author = self.request.user)