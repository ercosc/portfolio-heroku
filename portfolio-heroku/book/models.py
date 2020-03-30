from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=120)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("book:book_detail", kwargs={"id": self.id})
