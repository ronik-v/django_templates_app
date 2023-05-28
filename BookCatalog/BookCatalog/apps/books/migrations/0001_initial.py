# Generated by Django 4.1.6 on 2023-02-19 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing_house', models.CharField(max_length=100, verbose_name='Издательство')),
                ('name', models.CharField(max_length=100, verbose_name='Название книги')),
                ('autor', models.CharField(max_length=100, verbose_name='Автор книги')),
                ('cover', models.ImageField(upload_to='', verbose_name='Обложка книги')),
                ('genre', models.CharField(choices=[('Художественный', 'Художественная литература'), ('Научный', 'Научная литература'), ('Философский', 'Философская литература'), ('Психологический', 'Психологическая литература'), ('Искусство', 'Литература про искусство')], max_length=50, verbose_name='Жанр книги')),
                ('year', models.IntegerField(verbose_name='Год издания')),
                ('description', models.TextField(verbose_name='Описание книги')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor_name', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('text', models.CharField(max_length=300, verbose_name='Текст комментария')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
    ]