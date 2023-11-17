from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

from .views import BooksListAPIView, BookDetailAPIView

urlpatterns = [
    path('list/<int:pk>', BookDetailAPIView.as_view()), # with primary key
    path('list/', BooksListAPIView.as_view()), # search

]