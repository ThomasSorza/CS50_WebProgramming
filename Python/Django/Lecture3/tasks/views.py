from django.shortcuts import render

#from Python.Django.Lecture3 import tasks

tasks = ["foo", "bar", "baz"]
# Create your views here.
def index(request):
    return render(request,"tasks/index.html", { 
        "tasks" : tasks
    })

def add(request):
    return render(request,"tasks/add.html")