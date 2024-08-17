from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]


    def __str__(self):
        return (f"{self.title} by {self.author}")

class Library(models.Model):
    name = models.CharField(max_length=250)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=250)
    library = models.OneToOneField(Library, on_delete= models.CASCADE)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    role = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarians'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=role, default='Member')
