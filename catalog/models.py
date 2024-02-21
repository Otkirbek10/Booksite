from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200,verbose_name='Title of a book')
    book_slug = models.SlugField(max_length=200,unique=True,null=True)
    genre = models.ForeignKey('Genre',on_delete=models.CASCADE,verbose_name='Genre of a book')
    language = models.ForeignKey('Language',on_delete=models.CASCADE,verbose_name='language of a book')
    author = models.ManyToManyField('Author',verbose_name='Authors of a book')
    photo = models.ImageField(upload_to='book_images/',null=True,blank=True,verbose_name='Photo of a book')
    description = models.TextField(max_length=1500,verbose_name='About a book')
    isbn = models.CharField(max_length=13,verbose_name='ISBN of a book')

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail',args=str[self.id])


class Genre(models.Model):
    name = models.CharField(max_length=200,verbose_name='Genre books')

    def __str__(self) -> str:
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20,verbose_name='Language')

    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    full_name = models.CharField(max_length=200,verbose_name="Author's name")
    slug = models.SlugField(max_length=200,unique=True,null=True)
    picture = models.ImageField(upload_to='authors/',null=True,verbose_name="Author's photo")
    date_of_birth = models.DateField(null=True,blank=True,verbose_name='Date of birth')
    date_of_death = models.DateField(null=True,blank=True,verbose_name='Date of death')
    biography = models.TextField(null=True,verbose_name='Biography of an author')

    def __str__(self) -> str:
        return self.full_name

class Status(models.Model):
    name = models.CharField(max_length=20,verbose_name='Copy status of a book')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Statuses"

class BookInstance(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    inv_nom = models.CharField(max_length=20,null=True,verbose_name='Inventory number')
    imprint = models.CharField(max_length=200,verbose_name='Publishing house')
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=True,verbose_name='Book copy status')
    due_back = models.DateField(null=True,blank=True,verbose_name='Staus expire date')

    def __str__(self):
        return '%s - %s - %s' % (self.inv_nom, self.book, self.status)
