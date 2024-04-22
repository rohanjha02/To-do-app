from django.shortcuts import render
from .models import TodoListItem 
from django.http import HttpResponseRedirect 
# Create your views here.
def index(request):
    return render(request, 'index.html')



def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',  {'all_items':all_todo_items})


def addTodoView(request):
    new_item = TodoListItem()
    new_item.content = request.POST.get('content')
    new_item.save()
    return HttpResponseRedirect('/todo/') 


def deleteTodoView(request, id):
    y = TodoListItem.objects.get(id= id)
    y.delete()
    return HttpResponseRedirect('/todo/') 


