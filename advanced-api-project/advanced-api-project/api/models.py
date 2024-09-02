from django.db import models

# Create your models here.
class Author(models.Model): ## this creates the Author model.
    name = models.CharField(max_length=255) ## creates the name field for Author model.
    
    def __str__(self):
        return self.name
    
class Book(models.Model): ## this creates the Book model.
    title = models.CharField(max_length=255) ## creates title field for Book modle.
    publication_year = models.IntegerField() ## creates the publication year field for Book modle.
    author = models.ForeignKey(Author, on_delete=models.CASCADE) ## this links the Book model and Author model in many to one relation.

    def __str__(self):
        return self.title