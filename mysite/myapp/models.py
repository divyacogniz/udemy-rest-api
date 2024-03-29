from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
# from django.contrib.auth.models import
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):

    def create_user(self,name,email,password=None):
        if not email:
            raise ValueError(' user email must be  unique and valid')
        email=self.normalize_email(email)
        user=self.models(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_super_user(self,email,name,password):

        user=self.craete_user(email,password,name)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name
    def __str__(self):
        return self.email
