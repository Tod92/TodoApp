from django.shortcuts import render
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
    # result = [str(t) for t in tasks]
    return render(request,
                  'todo/index.html',
                  context=context
                  )
