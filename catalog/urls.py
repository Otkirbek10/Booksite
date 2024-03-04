from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    re_path('^books/$',books_list, name="books"),
    path('book/<slug:book_slug>/',book_detail,name="book_detail"),
    path("authors/author/<slug:slug>/",book_author,name='author'),
    path('book/genre/<int:id>/',book_genre, name="book_genre"),
    path('authors/',authors,name='authors'),
    path('search/',search,name='search'),
    path('sign_up',sign_up,name='sign_up'),
    path('log_out',log_out,name='log_out'),
    path('sign_in',sign_in,name='sign_in'),
    path('edit/<slug:book_slug>/',edit_book,name='edit'),
    path('delete/<slug:book_slug>/',delete_book,name='delete')

]





# {% extends 'base.html' %}


# {% block content %}
#     {% if book.photo %}
#         <img src="{{ book.photo.url }}" alt="Ok">
#     {% endif %}
#     <h1>Title of the book: {{ book.title }}</h1>
#     <p><strong>Genre:</strong> {{ book.genre }}</p>
#     <p><strong>Description:</strong> {{ book.description }}</p>
#     <p><strong>ISBN:</strong> {{ book.isbn }}</p>
#     <p><strong>Language:</strong> {{ book.language }}</p>
#         {% for author in book.author.all %}     
#             <p><strong>Author:</strong>
#                 <a href="">{{ author.full_name }}</a></p>
#         {% endfor %}

# <div style="margin-left: 20px;margin-top: 20px;">
#     <h4>Amount of the copies</h4>
#     {% for copy in book.book_instance_set.all %}
#         <hr><p class="{% if copy.status == 1 %} text-succes
#                          {% elif copy.status == 2 %} text-danger
#                          {% else %} text-warning
#                          {% endif %}">{{copy.get_status_display}}</p>
            
#         <p><strong>Pulishing house</strong>{{ copy.imprint }}</p>
#         <p class="text-muted"><strong>Inventory number</strong>{{ copy.id }}</p>
#         <p><strong>Status of copy</strong>{{ copy.status }}</p>

#     {% endfor %}
# </div>

# {% endblock %}
# <p><strong>Author:</strong><a href="">{{ author.full_name }}</a></p>

