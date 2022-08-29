from rest_framework import serializers
from .models import Author
from notes.models import Note

class AuthorSerializer(serializers.ModelSerializer):
    notes = serializers.StringRelatedField(many = True, read_only = True)
    
    class Meta:
        model = Author
        fields = ['username', 'email', 'notes']