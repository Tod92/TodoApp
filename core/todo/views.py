from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Task
# Create your views here.
def index(request):
    tasks = Task.objects.filter(
        Q(status="TODO") | Q(status="DOING")
    )
    result = [str(t) for t in tasks]
    return HttpResponse("Hello there general Kenobi" + str(result))
