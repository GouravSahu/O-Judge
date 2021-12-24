from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from .models import Problems
from .models import Testcase

import subprocess,os,time
from subprocess import PIPE

import filecmp


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
    fs = FileSystemStorage(location=folder) #defaults to MEDIA_ROOT  
    filename = fs.save(myfile.name, myfile)
    
    cmd="media/"+ myfile.name
    
    data=subprocess.Popen(["docker","start", "my-gcc"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    data.communicate()

    data=subprocess.Popen(["docker","cp",cmd,"my-gcc:/gourav.cpp"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    data.communicate()

    data=subprocess.Popen(["docker","cp", "media/tests.txt","my-gcc:/tests.txt"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    data.communicate()

    data=subprocess.Popen(["docker","cp", "media/out.txt","my-gcc:/out.txt"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    data.communicate()

    data=subprocess.Popen(["docker", "exec", "my-gcc","g++","gourav.cpp", "./a.out"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    data.communicate()

    command= 'docker exec -ti my-gcc sh -c "./a.out <tests.txt > out.txt"'

    data=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True)
    data.communicate()

    command2= "docker cp my-gcc:out.txt media/out.txt"
    data=subprocess.Popen(command2,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True)
    data.communicate()

    f1="media/myout.txt"
    f2="media/out.txt"
    
    result = filecmp.cmp(f1, f2, shallow=False)

    verdict=""
    if result==True:
        verdict="All test cases Passed"
    else:
        verdict="Please try again"
    return render(request,'online_judge/finalpage.html',{'name':verdict,'question':question_id})
    


# Create your views here.
