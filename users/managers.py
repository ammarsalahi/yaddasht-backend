from django.db import models
from django.contrib.auth.models import UserManager as AbstractUserManager

class UserManager(AbstractUserManager):
    def create_user(self,email,username,password):
        if not username:
            raise('username is not entered!')
        if not email:
            raise('email is not entered!')
        user=self.model(
            email=email,
            username=username
        )
        user.set_password(password)    
        user.save(self._db)
        return user
    def create_superuser(self,email,username,password):
        user=self.create_user(
            email=email,
            password=password,
            username=username

        )
        user.is_superuser=True
        user.is_staff=True
        user.is_admin=True
        user.save()
        return user
    def create_publicuser(self,email,username,password):
        user=self.create_user(
            email=email,
            password=password,
            username=username
        ) 
        user.save()
        return user       
