from django.urls import path, include
from rest_framework.authtoken import views as authview

from libraryapp import views

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api-token-auth/', authview.obtain_auth_token, name='api-token-auth'),
    path('add-author/', views.add_author, name='add-author'),
    path('get-author/', views.get_authors, name='get-author'),
    path('update-author/<int:pk>/', views.update_author, name='update-author'),
    path('author/<int:pk>/delete', views.delete_author, name='delete-author'),
    path('add-book/', views.add_book, name='add-book'),
    path('get-book/', views.get_books, name='get-book'),
    path('update-book/<int:pk>/', views.update_book, name='update-book'),
    path('book/<int:pk>/delete', views.delete_book, name='delete-book'),
    path('book-author-name/', views.book_by_author_name, name='book-author-name'),
    path('books-published-date/', views.book_by_published_date, name='books-published-date'),
]
