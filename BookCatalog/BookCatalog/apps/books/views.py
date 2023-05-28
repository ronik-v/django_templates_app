from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Book


def index(request):
	all_books_genre = Book.GENERS_LIST
	return render(request, 'books/list.html', {'all_books_genre': all_books_genre})


def detail(request, genre):
	try:
		Books = Book.objects.filter(genre__in=(genre, genre))
	except:
		raise Http404('Книги не найденны!')

	#Comments = Books.comment_set.order_by('-id')
	return render(request, 'books/detail.html', {'Books': Books})


def leave_comment(request, genre):
	try:
		Books = Book.objects.filter(genre__in=(genre, genre))
	except:
		raise Http404('Книги не найденны!')
	Books.comment_set.create(autor_name=request.POST['name'], text=request.POST['text'])
	return HttpResponseRedirect(reverse('books:detail', args=((genre, genre),)))
