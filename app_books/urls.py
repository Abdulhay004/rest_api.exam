from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

from .views import (BooksListAPIView,
                    BookDetailAPIView,
                    BookCreateAPIView,
                    BookUpdateAPIView)

urlpatterns = [
    path('list/<int:pk>', BookDetailAPIView.as_view()), # with primary key
    path('list/', BooksListAPIView.as_view()), # search
    path('new', BookCreateAPIView.as_view()),
    path('update/<int:pk>', BookUpdateAPIView.as_view()),

]