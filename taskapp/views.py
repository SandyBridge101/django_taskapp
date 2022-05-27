from multiprocessing import context
from pyexpat import model
from django.forms import Form
from django.shortcuts import render,redirect
from . models import TaskModel
from . forms import TaskModelForm, TaskUpdateForm
from django.http import HttpResponse#import http.Response
# Create your views here.

def index(request):
    if request.method=='POST':#if there is a request to post
        form=TaskModelForm(request.POST)
        if form.is_valid():#if it meets all contraints. mine worked without the brackets
            form.save()
            return redirect('/')
    else:
        form=TaskModelForm()

    data=TaskModel.objects.all().order_by('-date')# the same as TaskModel.objects.raw('select * from "taskapp_Taskmodel" ')
    total_task=data.count()
    completed_task=TaskModel.objects.filter(isComplete=True).count()
    uncompleted_task=total_task-completed_task
    context={
        'data':data,
        'form':form,
        'total_task':total_task,
        'completed_task':completed_task,
        'uncompleted_task':uncompleted_task,
    }
    
    return render(request,"index.html",context)#loads the html file.passes in data from the modles file

def about(request):
    return render(request,"about.html")

def delete(request,pk):
    item=TaskModel.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    return render(request,"delete.html")

def edit(request,pk):
    item=TaskModel.objects.get(id=pk)

    if request.method=='POST':
        form=TaskUpdateForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=TaskUpdateForm(instance=item)


    context={
        'form':form
    }
    return render(request,'edit.html',context)
"""
def index(request):
    return HttpResponse("HomePage")


def about(request):
    return HttpResponse("About Page")
"""