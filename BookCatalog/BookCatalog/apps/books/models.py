from django.db import models


class Book(models.Model):
	GENRES_CHOICES = [
		('Художественная', 'Художественная'),
		('Научная', 'Научная'),
		('Философская', 'Философская'),
		('Психологическая', 'Психологическая'),
		('Искусство', 'Искусство')
	]
	GENERS_LIST = [name[1] for name in GENRES_CHOICES]
	publishing_house = models.CharField('Издательство', max_length=100)
	name = models.CharField('Название книги', max_length=100)
	autor = models.CharField('Автор книги', max_length=100)
	cover = models.ImageField('Обложка книги')
	genre = models.CharField('Жанр книги', max_length=50, choices=GENRES_CHOICES)
	year = models.IntegerField('Год издания')
	description = models.TextField('Описание книги')

	@classmethod
	def __str__(cls):
		return f'{cls.name}'

	class Meta:
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'


class Comment(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	autor_name = models.CharField('Имя автора', max_length=50)
	text = models.CharField('Текст комментария', max_length=300)

	@classmethod
	def __str__(cls):
		return f'{cls.autor_name}'

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

