from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    books = Book.objects.all().count()
    authors = Author.objects.all().count()
    instances = BookInstance.objects.all().count()
    return render(request,'catalog/index.html',context={'books':books,'authors':authors,'instances':instances})


