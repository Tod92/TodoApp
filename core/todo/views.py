from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.filter(
        Q(status="TODO") | Q(status="DOING")
    )
    context = {
        "tasks": tasks
    }
    return render(request,
                  'todo/index.html',
                  context=context)

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        print(title)
        if title:
            task = Task.objects.create(title=title)
            return render(request, 'todo/task_item.html', {'task': task})
    return HttpResponse(status=400)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return HttpResponse('')

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return render(request, 'todo/task_item.html', {'task': task})