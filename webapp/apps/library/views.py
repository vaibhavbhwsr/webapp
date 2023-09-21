from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class BookView(TemplateView):
    template_name = "library/books.html"
