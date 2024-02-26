from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
from django.views import generic

def index(request):
    books = Book.objects.all().count()
    authors = Author.objects.all().count()
    return render(request,'catalog/index.html',context={'books':books,'authors':authors})


def books_list(request): 
    genres = Genre.objects.all()
    books = Book.objects.all()
    return render(request, "catalog/books.html", {'genres': genres, 'books': books}) 


def book_detail(request, book_slug):
    book = get_object_or_404(Book, book_slug=book_slug)
    return render(request,'catalog/book_detail.html', {'book': book})

def book_author(request,slug):
    author = get_object_or_404(Author,slug=slug)
    books = Book.objects.filter(author=author)
    return render(request,'catalog/author.html',{'author':author,'books':books})
    