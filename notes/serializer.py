from dataclasses import field
from rest_framework import serializers
from notes.models import Note

class NoteSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = Note
        fields = '__all__'
    
    def create(self, validated_data):
        return Note.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.save()
        return instance
