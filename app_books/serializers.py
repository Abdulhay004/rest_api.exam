from rest_framework.serializers import ModelSerializer

from .models import Books


class BooksSerializer(ModelSerializer):
    class Meta(ModelSerializer):
        model = Books
        fields = ['id', 'book_title', 'book_price', 'book_image']
        # fields = '__all__'


class BookDetailsSerializer(ModelSerializer):
    class Meta(ModelSerializer):
        model = Books
        # fields = ['id', 'book_title', 'book_price', 'book_image']
        fields = '__all__'