from django.shortcuts import render,redirect,reverse
from django.http import Http404 , HttpResponse,HttpResponseRedirect
from poll.models import *

# Create your views here.
def index(request):
    context = {}
    questions = Question.objects.all()
    context['tittle'] = 'polls'
    context['questions'] = questions
    return render(request,'index.html',context)


def details(request,id):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context['question'] = question
    return render(request,'detail.html',context)

def poll(request,id=None):
    context = {}
   
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
        
    context['question'] = question
    if request.method == "POST":
        user_id = 1
        data = request.POST
        ret = Answer.objects.create(user_id=user_id,choice_id=data['answer'])
        if ret:
            return HttpResponseRedirect(reverse('details_page',args=[question.id]))

        else:
            context["error"] = "your vote is not done successfully"
            return render(request,'poll.html',context)
    else:
        return render(request,'poll.html',context)
