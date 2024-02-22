from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'slug', 'date_of_birth', 'date_of_death')
    fields = ['full_name', 'slug', 'picture', 'biography', ('date_of_birth', 'date_of_death')]
    prepopulated_fields = {"slug": ("full_name",)}

admin.site.register(Author,AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'genre', 'language', 'photo', 'isbn')
    list_filter = ('genre', 'author', 'language')
    prepopulated_fields = {"book_slug": ("title",)}
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book','status')
    fieldsets = (
        ('Copy of the book',{
            'fields': ('book','imprint','inv_nom')
        }),
        ('Status and expiry date',{
            'fields': ('status','due_back')
        }),
    )



admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)

