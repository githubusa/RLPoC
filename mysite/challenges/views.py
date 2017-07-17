from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #context = {'latest_question_list': latest_question_list}
    #return render(request, 'polls/index.html', context)
    return HttpResponse("Hello world. You're in the reading challenges.")
