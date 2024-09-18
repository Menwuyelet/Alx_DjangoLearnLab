from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email,username, password):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('The Username is required')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using= self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(email=email, username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class CustomUser(AbstractUser):
    email = models.EmailField(unique= True, max_length= 255)
    username = models.CharField(unique =True, max_length= 15)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username