from rest_framework import serializers

from notes.models import Note

class NoteSerial(serializers.ModelSerializer):
    bg_color=serializers.CharField(read_only=True)
    class Meta:
        model=Note
        fields=('title','body','image','user','bg_color','id')
    
    def create(self, validated_data):
        return Note.obj.create_note(**validated_data)
