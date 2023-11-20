from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView,
                                     UpdateAPIView)
from rest_framework.views import APIView
from django.http import HttpResponse

from .models import Books
from .serializers import BooksSerializer, BookDetailsSerializer


# Create your views here.
class BooksListAPIView(ListAPIView):
    # queryset = Books.objects.all()
    serializer_class = BooksSerializer

    def get_queryset(self):
        if 'name' in self.request.GET and 'value' in self.request.GET:
            match self.request.GET['name']:
                case 'title':
                    # icontains -> ichida qatnashsa
                    key_word = self.request.GET['value']
                    queryset = Books.objects.filter(book_title__icontains=key_word)
                case 'author':
                    key_word = self.request.GET['value']
                    queryset = Books.objects.filter(book_author__icontains=key_word)
                case _: # all | else
                    key_word = self.request.GET['value']
                    queryset = Books.objects.filter(book_desc__icontains=key_word) | Books.objects.filter(book_price__icontains=key_word)


        else:
            queryset = Books.objects.all()
        # if 'filter' in self.request.GET:
        if 'from' in self.request.GET and 'to' in self.request.GET:
            if 'to' not in self.request.GET:
                start_price = self.request.GET['from']
                queryset = queryset.filter(book_price__gte=start_price)
            elif 'from' not in self.request.GET:
                final_price = self.request.GET['to']
                queryset = queryset.filter(book_price__lte=final_price)
            else:
                start_price = self.request.GET['from']
                final_price = self.request.GET['to']
            queryset = queryset.filter(book_price__range=(start_price, final_price))


        return queryset


class BookDetailAPIView(RetrieveAPIView):
    serializer_class = BookDetailsSerializer
    queryset = Books.objects.all()


class BookCreateAPIView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
class BookUpdateAPIView(UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
