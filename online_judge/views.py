from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


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


def finalpage(request,question_id,form_id):
    folder='media/'
    myfile = request.FILES['file']
    fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT  
    filename = fs.save(myfile.name, myfile)
    return render(request,'online_judge/finalpage.html',{'name':myfile.name})
    



# Create your views here.
