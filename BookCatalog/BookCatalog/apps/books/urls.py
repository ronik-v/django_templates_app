from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
	path('', views.index, name='index'),
	path('<str:genre>/', views.detail, name='detail'),
	path('<str:genre>/leave_comment', views.leave_comment, name='leave_comment')
]
