from django.contrib import admin
from .models import Book, Author, Publisher, Genre

# Register your models here.

admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
