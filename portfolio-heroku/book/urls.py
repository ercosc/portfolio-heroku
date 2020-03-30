from django.urls import path
from .views import Book_list, Book_detail, Book_create, Book_update, Book_delete


app_name = 'book'
urlpatterns = [
    path('', Book_list.as_view(), name='book_list'),
    path('<int:id>/', Book_detail.as_view(), name='book_detail'),
    path('create/', Book_create.as_view(), name='book_create'),
    path('<int:id>/update/', Book_update.as_view(), name='book_update'),
    path('<int:id>/delete/', Book_delete.as_view(), name='book_delete')
]
