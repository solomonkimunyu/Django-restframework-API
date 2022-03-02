from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Book

class BookView(ListView):
    model = Book
    template_name = 'book_list.html'