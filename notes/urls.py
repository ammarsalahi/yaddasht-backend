from rest_framework.routers import DefaultRouter
from notes.api import NoteViewset

router=DefaultRouter()
router.register('',NoteViewset,basename='notes-api')

urlpatterns=router.urls