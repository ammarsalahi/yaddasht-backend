from rest_framework.viewsets import ModelViewSet
from notes.serializers import NoteSerial
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

class NoteViewset(ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=NoteSerial
    filter_backends=[filters.SearchFilter]
    search_fields=['title','body']
    def get_queryset(self):
        return self.request.user.notes.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)