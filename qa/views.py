from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Question, Answer


def list_new_questions(request):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'new_list.html', {'questions': page.object_list, 'paginator': paginator, 'page': page,})

def list_popular_questions(request):
    questions = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'new_list.html', {'questions': page.object_list, 'paginator': paginator, 'page': page, })



def question_detail(request, pk):
    question = get_object_or_404(Question,pk=pk)
    print(question.q_anwsers.all())
    return render(request, 'detail.html', {'question': question, 'answers': question.q_anwsers.all} )