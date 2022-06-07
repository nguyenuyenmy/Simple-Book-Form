from django.db import models


# Create your models here.
class Author(models.Model):
    author_id = models.CharField(max_length=256, unique=True)
    author_name = models.CharField(max_length=256)
    birthdate = models.DateField()

    def __str__(self):
        return self.author_name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_id = models.CharField(max_length=256, unique=True)
    book_name = models.CharField(max_length=256)
    published_date = models.DateField()

    def __str__(self):
        return self.book_name
