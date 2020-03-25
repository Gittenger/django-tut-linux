"""Define views here."""
from django.shortcuts import render

from .models import Question  # ,Choice

# Get questions and display them


def index(request):
    """Return index view."""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context is accessed in template by key names, which will ref the value
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
