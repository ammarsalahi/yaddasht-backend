from email.mime import image
from nturl2path import url2pathname
from django.db import models
from django.forms import CharField
import random
# Create your models here.
colors=[
    '#f44336','#e91e63','#9c27b0',
    '#673ab7','#3f51b5','#2196f3',
    '#03a9f4','#00695f','#4caf50',
    '#8bc34a','#cddc39','#ffeb3b',
    '#ffc107','#ff9800','#ff5722'
]
class NoteManager(models.Manager):
    def create_note(self,title,body,user,image=None):
        note=self.model(
            title=title,
            body=body,
            user=user,
            bg_color=random.choice(colors)
        )
        if image is not None:
            note.image=image
        note.save(self._db)
        return note

class Note(models.Model):

    user=models.ForeignKey('users.User',related_name='notes',on_delete=models.CASCADE)
    title=models.CharField(verbose_name='عنوان',max_length=500,blank=True, null=True)
    body=models.TextField(verbose_name='متن',blank=True,null=True)
    image=models.ImageField(verbose_name='تصویر',upload_to='imgs/',blank=True, null=True)
    bg_color=models.CharField(max_length=10)
    create_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='یاددشت'
        verbose_name_plural='یادداشت ها'
    
    objects=models.Manager()
    obj=NoteManager()
    def get_title(self):
        return self.title
    def get_body(self):
        return self.body
    def get_img(self):
        return self.image.url
     
