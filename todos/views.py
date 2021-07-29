from django.shortcuts import render, redirect

from .models import Todo


def new(request):
    return render(request, 'new.html')


def create(request):
    Todo(
        title=request.GET.get('title'),
        content=request.GET.get('content'),
        due_date=request.GET.get('due-date'),
    ).save()
    return redirect('/todos/')


def index(request):
    context = {
        'todos': Todo.objects.order_by('due_date').all(),
    }
    return render(request, 'index.html', context)


def detail(request, todo_id):
    context = {
        'todo': Todo.objects.get(id=todo_id),
    }
    return render(request, 'detail.html', context)


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/todos/')


def edit(request, todo_id):
    context = {
        'todo': Todo.objects.get(id=todo_id),
    }
    return render(request, 'edit.html', context)


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.title = request.GET.get('title')
    todo.content = request.GET.get('content')
    todo.due_date = request.GET.get('due-date')
    todo.save()
    return redirect(f'/todos/{todo_id}/detail')
