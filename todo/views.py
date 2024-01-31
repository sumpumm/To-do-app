from django.shortcuts import render,redirect
from .models import Task

# Create your views here.

def index(request):
    task=Task.objects.all()
    context={
        'task':task,
    }
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def create(request):
    context={}
    if request.method=="POST":
      title=request.POST.get('title')  
      description=request.POST.get('desc')
      if title=="" or description=="":
          context['error']='Fields cannot be empty'
          return render(request,'create.html',context)
      Task.objects.create(
          title=title,
          description=description
      )
      return redirect('/')    
    return render(request,'create.html',context)

def mark_completed(request,pk):
    task=Task.objects.get(pk=pk)
    task.is_completed=True
    task.save()
    return redirect('/')  

def delete(request,pk):
    context={
        'task':Task.objects.all()
    }
    task=Task.objects.get(pk=pk)
    task.delete()
    context['delete']='deleted successfully'
    return render(request,'index.html',context)

def edit(request,pk):
    task=Task.objects.get(pk=pk)
    if request.method=="POST":
        title=request.POST.get('title')  
        description=request.POST.get('desc')
        task.title=title
        task.description=description
        task.save()
        return redirect('/')  
    
    return render(request,'edit.html')
    