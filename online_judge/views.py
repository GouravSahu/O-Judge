from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


from .models import Problems
from .models import Testcase


def index(request):
    question_name=Problems.objects.all()
    template=loader.get_template('online_judge/index.html')
    context={
        'question_name':question_name,
    }
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    question = Problems.objects.get(pk=question_id)
    testcases= question.testcase_set.all()
    return render(request, 'online_judge/detail.html', {'question': question,'testcases':testcases})



    



# Create your views here.
