from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from . import forms

# Create your views here.

from django.http import HttpResponse

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #return HttpResponse("Hello world. You're the polls index.")
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': 'a'}
    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = forms.SignUpForm()
    return render(request, 'signup.html', {'form': form})
