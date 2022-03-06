from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('singe_book/<int:id>', views.single_book,name='single_book'),
    path('register', views.create_librarian,name='register'),
    path('login', views.librarian_login,name='login'),
    path('logout', views.librarian_logout, name='librarian_logout'),
    path('book', views.book_crud,name='book'),
    path('book/<int:id>', views.book_delet,name='delete'),
    path('book_edit/<int:id>', views.book_edit,name="book_edit"),
    path('book_u/<int:id>', views.book_u,name="book_u"),
]
