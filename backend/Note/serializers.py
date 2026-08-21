from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'is_public', 'owner']