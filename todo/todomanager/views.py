from django.shortcuts import redirect, render

from .models import TodoItem


# Create your views here.
def index(request):
    todoItems = TodoItem.objects.all()
    return render(request, 'index.html', {'todoItems': todoItems})

def create(request):
    newTodoItem = TodoItem(title=request.POST['title'], description=request.POST['description'], completed=False)
    newTodoItem.save()
    return redirect('index')

def createPage(request):
    return render(request, 'create.html')

def delete(request, id):
    todoItem = TodoItem.objects.get(id=id)
    todoItem.delete()
    return redirect('index')

def update(request, id):
    if request.method == 'POST':
        print(request.POST)
        todoItem = TodoItem.objects.get(id=id)
        todoItem.title = request.POST['title']
        todoItem.description = request.POST['description']
        todoItem.completed = 'completed' in request.POST and request.POST['completed'] == 'on'
        todoItem.save()
        return redirect('index')
    
    return render(request, 'update.html', {'todo': TodoItem.objects.get(id=id)})

def complete(request, id):
    todoItem = TodoItem.objects.get(id=id)
    todoItem.completed = True
    todoItem.save()
    return redirect('index')

def notComplete(request, id):
    todoItem = TodoItem.objects.get(id=id)
    todoItem.completed = False
    todoItem.save()
    return redirect('index')