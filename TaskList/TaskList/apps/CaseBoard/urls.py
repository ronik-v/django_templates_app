from django.urls import path
from . import views

app_name = 'CaseBoard'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:CaseBoard_id>/', views.detail, name='detail'),
    path('<int:CaseBoard_id>/leave_comment/', views.leave_comment, name='leave_comment')
]