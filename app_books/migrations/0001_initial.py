# Generated by Django 3.2.12 on 2023-11-17 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50, verbose_name='Book name')),
                ('book_author', models.CharField(max_length=255, verbose_name='Book author')),
                ('book_price', models.IntegerField(verbose_name='Book price')),
                ('book_desc', models.CharField(max_length=255, verbose_name='Book description')),
                ('book_image', models.ImageField(upload_to='books')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]