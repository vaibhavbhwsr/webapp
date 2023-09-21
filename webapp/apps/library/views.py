from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

# Create your views here.


class BookView(ListView):
    model = Book
    template_name = "library/books.html"
