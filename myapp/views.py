from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .form import createNewTask, createNewProject
# Create your views here.
def index(request):
    return render(request,"index.html")

def hello(request, username  ):
    print(username)
    return HttpResponse("<h1>hello %s</h1>" %username)

def about(request):
    return render(request, "about.html")

def project(request):
    project=Project.objects.all()
    return render(request,"project.html",{
        "project":project
        })
    # return JsonResponse(project, safe=False)


def task(request):
    task=Task.objects.all()
    return render(request,"task.html", {"task":task})

def create_task(request):
    if request.method == 'GET':
        return render(request,'create_task.html',{'form': createNewTask()})
    else:
        Task.objects.create(
            title=request.POST['title'], descripcion=request.POST['descripcion'],project_id=2)
        return redirect('task')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html',{'form':createNewProject()})
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('project')

