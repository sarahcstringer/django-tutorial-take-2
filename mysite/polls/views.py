from django.shortcuts import render, get_object_or_404
from .models import Question


# Create your views here.
def index(request):
    """Display 5 most recent questions"""

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """Display the details of an individual question"""

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """Display the results of a question's votes"""

    return render(request, 'polls/results.html')

def vote(request, question_id):
    """Vote for a question"""

    return render(request, 'polls/vote.html')