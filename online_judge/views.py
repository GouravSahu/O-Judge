from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from .models import Problems
from .models import Testcase

import subprocess,os,time
from subprocess import PIPE


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

def calculate(name):
    cmd="media/"+name
    i_file=open("media/tests.txt","r")
    args=[]
    for line in i_file:
        stripped_line=line.strip()
        listofline=stripped_line.split()
        for l in listofline:
            args.append(l)

    i_file.close()    
    data=subprocess.Popen(["g++",cmd,"-o","a"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    data.communicate()

    outlist=[]
    for i in range(len(args)):
        d = subprocess.Popen(["echo",args[i],"|","a.exe"], stdin=PIPE, stdout=subprocess.PIPE, universal_newlines=True,shell=True)  
        outlist.append(d.communicate()[0])
    return outlist




def finalpage(request,question_id,form_id):
    folder='media/'
    myfile = request.FILES['file']
    fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT  
    filename = fs.save(myfile.name, myfile)
    outfile=[]
    outfile=calculate(myfile.name)
    o_file=open("media/out.txt","r")
    realoutlist=[]
    for line in o_file:
        stripped_line=line.strip()
        listofline=stripped_line.split()
        for l in listofline:
            realoutlist.append(l)
    
    verdict=""
    if realoutlist==outfile:
        verdict="All test cases Passed"
    else:
        verdict="Please try again"
    return render(request,'online_judge/finalpage.html',{'name':verdict})
    



# Create your views here.
