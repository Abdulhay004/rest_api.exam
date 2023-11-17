from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.http import HttpResponse

from .models import Books
from .serializers import BooksSerializer, BookDetailsSerializer


# Create your views here.
class BooksListAPIView(ListAPIView):
    # queryset = Books.objects.all()
    serializer_class = BooksSerializer

    def get_queryset(self):
        if 'book' in self.request.GET:
            key_word = self.request.GET['book']
            queryset = Books.objects.filter(book_title__icontains=key_word)
        else:
            queryset = Books.objects.all()
        return queryset


class BookDetailAPIView(ListAPIView):
    serializer_class = BookDetailsSerializer
    pagination_class = None
    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Books.objects.filter(pk=pk)
        return queryset
#
# def greetings(request):
#     return HttpResponse('<h1>Hello world</h1>')