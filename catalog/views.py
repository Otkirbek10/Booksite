from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import *
from django.views import generic
from django.db.models import Q
from django.shortcuts import redirect

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

def book_genre(request,id):
    genre = Genre.objects.get(pk = id)
    genres = Genre.objects.all()
    books = Book.objects.filter(genre_id = id)
    return render(request,'catalog/book_genre.html',{"genre":genre,'books':books,'genres':genres})

def authors(request):
    authors = Author.objects.all()
    return render(request,'catalog/authors.html',{"authors":authors})


def search(request):
    query = request.GET.get('query')
    books = Book.objects.filter(
        Q(title__icontains = query) |
        Q(description__icontains = query)
    )
    if books:
        return render(request,'catalog/search.html',{"books":books})
    else:
        return redirect('books')