from django.db import models


# Create your models here.
class Books(models.Model):
    book_title = models.CharField(max_length=50, verbose_name='Book name')
    book_author = models.CharField(max_length=255, verbose_name='Book author')
    book_price = models.IntegerField(verbose_name='Book price')
    book_desc = models.CharField(max_length=255, verbose_name='Book description')
    book_image = models.ImageField(upload_to='books')

    def __str__(self):
        return f"{self.id}. {self.book_title}"

    class Meta:
        db_table = 'books'
