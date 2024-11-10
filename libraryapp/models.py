from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=255, verbose_name="Author Name")
    date_of_birth = models.DateField(verbose_name="Date of Birth")


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Author Name")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField(verbose_name="Published Date")
    genre = models.CharField(max_length=100, verbose_name="Genre")
    is_archived = models.BooleanField(default=False)
