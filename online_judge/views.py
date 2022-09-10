from pdb import post_mortem
from pickle import FALSE
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from .models import Problems
from .models import Testcase
from .models import studentData

import subprocess,os,time
from subprocess import PIPE



def mainPage(request):
    return render(request,'online_judge/main-page.html')


def login(request,login):
    return render(request,'online_judge/login.html')


def forget(request,login,forget=2003):
    return render(request,'online_judge/forget.html')

def signup(request,login,signup):
    return render(request,'online_judge/signUp.html')

def update(request,login,forget=2003,update=18):
    if request.method=='POST':
        email=request.POST.get('email',False)
        password=request.POST.get('password',False)
        stemail=studentData.objects.get(sEmail=email)
        stemail.sPassword=password
        stemail.save()
    else:
        return render(request,'online_judge/login-checking.html')
    
    return render(request,'online_judge/login-checking.html')

def index(request,login,signup,index):
    if request.method=='POST':
        email=request.POST.get('email',False)
        stemail=studentData.objects.filter(sEmail=email)
        if stemail:
            return render(request,'online_judge/signup.html',{'store':True})
        else:
            name=request.POST.get('name',False)
            password=request.POST.get('password',False)
            store= studentData(sEmail=email,sName=name,sPassword=password)
            store.save()
    else:
        return render(request,'online_judge/checking.html')
    stname=studentData.objects.get(sEmail=email)
    name=stname.sName
    question_name=Problems.objects.all()
    return render(request,'online_judge/index.html',{'question_name':question_name,'stdname':name})

def checking(request,login,signup,q_id):
    if request.method=='POST':
        emails=request.POST.get('email',False)
        passwords=request.POST.get('password',False)
    
    else:
        return render(request,'online_judge/checking.html')
    
    stdata=studentData.objects.filter(sEmail=emails)
    stpass=studentData.objects.filter(sPassword=passwords)

    storing=False
    if stdata and stpass:
        storing=True
            
    if storing==True:
        question_name=Problems.objects.all()
        stname=studentData.objects.get(sEmail=emails)
        fname=stname.sName
        return render(request,'online_judge/index.html',{'question_name':question_name,'stdname':fname})

    else:
        return render(request,'online_judge/checking.html')


'''
def index(request,id):
    question_name=Problems.objects.all()
    template=loader.get_template('online_judge/index.html')
    context={
        'question_name':question_name,
    }
    return HttpResponse(template.render(context,request))
    
'''



def detail(request,login,signup,index,question_id):
    question = Problems.objects.get(pk=question_id)
    testcases= question.testcase_set.all()
    return render(request, 'online_judge/detail.html', {'question': question,'testcases':testcases,'name':index})


    


def finalpage(request,login,signup,index,question_id,form_id):
    folder='media/'+str(question_id)
    myfile = request.FILES['file']
    fs = FileSystemStorage(location=folder) #defaults to MEDIA_ROOT  
    filename = fs.save(myfile.name, myfile)
    
    cmd="media/"+str(question_id)+"/"+ myfile.name
    
    subprocess.run("docker start my-gcc",shell=True)

    subprocess.run("docker cp "+cmd+" my-gcc:/gourav.cpp",shell=True)

    input="media/"+str(question_id)+"/tests.txt"
    subprocess.run("docker cp "+input+" my-gcc:/tests.txt",shell=True)

    output="media/out.txt"
    subprocess.run("docker cp "+output+" my-gcc:/out.txt",shell=True)

    subprocess.run("docker exec my-gcc g++ gourav.cpp ./a.out",shell=True)

    command= 'docker exec -ti my-gcc sh -c "./a.out <tests.txt > out.txt"' 

    subprocess.run(command,shell=True)
    
    subprocess.run("docker exec my-gcc rm -rf a.out",shell=True)

    command2= "docker cp my-gcc:out.txt " +"media/"+str(question_id)+"/out.txt"
    subprocess.run(command2,shell=True)

    f1="media/"+str(question_id)+"/my-out.txt"
    f2="media/"+str(question_id)+"/out.txt"
    
    file1=open(f1,"r")
    file2=open(f2,"r")

    lines1=file1.readlines()
    lines2=file2.readlines()


    if(lines1==lines2):
        verdict="All test cases Passed"
    else:
        verdict="Please try again"
        
    return render(request,'online_judge/finalpage.html',{'name':verdict,'question':question_id})
    


# Create your views here.
'''
 subprocess.run("sudo docker start my-gcc",shell=True)

    subprocess.run("sudo docker cp "+cmd+" my-gcc:/Gourav-Sahu.cpp",shell=True)

    subprocess.run("sudo docker cp media/tests.txt my-gcc:/tests.txt",shell=True)

    subprocess.run("sudo docker exec my-gcc g++ Gourav-Sahu.cpp ./a.out",shell=True)

    command= 'sudo docker exec -ti my-gcc sh -c "./a.out <tests.txt > out.txt"'

    subprocess.run(command,shell=True)

    command2= "sudo docker cp my-gcc:/out.txt media/out.txt"
    subprocess.run(command2,shell=True)
'''

'''
data=subprocess.Popen(["docker","start", "my-gcc"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    data.communicate()

    data=subprocess.Popen(["docker","cp",cmd,"my-gcc:/gourav.cpp"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    data.communicate()

    input="media/"+str(question_id)+"/tests.txt"
    data=subprocess.Popen(["docker","cp", input,"my-gcc:/tests.txt"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    data.communicate()

    output="media/out.txt"
    data=subprocess.Popen(["docker","cp", output,"my-gcc:/out.txt"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    data.communicate()

    data=subprocess.Popen(["docker", "exec", "my-gcc","g++","gourav.cpp", "./a.out"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    data.communicate()

    command= 'docker exec -ti my-gcc sh -c "./a.out <tests.txt > out.txt"'

    data=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True)
    data.communicate()

    data=subprocess.Popen(["docker", "exec", "my-gcc","rm","-rf", "a.out"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    data.communicate()

    ##command2= "docker cp my-gcc:out.txt media/out.txt"
    command2= "docker cp my-gcc:out.txt " +"media/"+str(question_id)+"/out.txt"
    data=subprocess.Popen(command2,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True)
    data.communicate()



'''