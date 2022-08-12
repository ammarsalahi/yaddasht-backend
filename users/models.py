from multiprocessing import managers
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

from users.managers import UserManager
# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True,verbose_name='ایمیل')

    class Meta:
        verbose_name='کاربر'
        verbose_name_plural='کاربران'   

    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    def get_name(self):
        return self.email