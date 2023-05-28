from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import CaseBoard
from django.urls import reverse


def index(request):
    all_things = CaseBoard.objects.all()
    return render(request, 'CaseBoard/list.html', {'all_things': all_things})


def detail(request, CaseBoard_id):
    try:
        Board = CaseBoard.objects.get(id=CaseBoard_id)
    except:
        raise Http404('Дело не найденно')
    comments = Board.comment_set.order_by('-id')
    return render(request, 'CaseBoard/detail.html', {'Board': Board, 'comments': comments})


def leave_comment(request, CaseBoard_id):
    try:
        Board = CaseBoard.objects.get(id=CaseBoard_id)
    except:
        raise Http404('Дело не найденно')
    Board.comment_set.create(text=request.POST['text'])
    return HttpResponseRedirect(reverse('CaseBoard:detail', args=(Board.id, )))
