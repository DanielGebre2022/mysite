from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publisher/', views.publisher, name='publisher'),
    path('author/', views.author, name='author'),
    path('book/', views.book, name='book'),
    path('newauthor/', views.newAuthor, name='newauthor'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]