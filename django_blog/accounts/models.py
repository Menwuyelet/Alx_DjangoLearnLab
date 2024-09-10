from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

class userManager(UserManager):
   def create_user(self, email, password):
          if not email:
               raise ValueError('Email is required.')
          user = self.model(email=self.normalize_email(email))
          user.set_pssword(password)
          user.save(using=self._db)
          return user
     
   def create_superuser(self, email, password):
          user = self.create_user(email = email, password=password)
          user.is_staff = True
          user.is_superuser = True
          user.save(using = self._db)
          return user

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=False, max_length=15)
    objects = userManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
          return self.username
