from django.urls import include, path
from django.conf import settings
from django.conf.urls import include, url
from .views import api_view, book_list_view


urlpatterns = [
    path(r'', api_view, name='api'),
    path(r'books', book_list_view, name='book-list-apo')
]