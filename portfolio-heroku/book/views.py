from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView,DeleteView
from .models import Book
from .forms import BookModelForm
from django.urls import reverse


class Book_delete(DeleteView):
    template_name = 'book/book_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)

    def get_success_url(self):
        return reverse('book:book_list')


class Book_create(CreateView):
    template_name = 'book/book_create.html'
    form_class = BookModelForm
    queryset = Book.objects.all()

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)


class Book_detail(DetailView):
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)


class Book_list(ListView):
    queryset = Book.objects.all()


class Book_update(UpdateView):
    template_name = 'book/book_update.html'
    form_class = BookModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)
