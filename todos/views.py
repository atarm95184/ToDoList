from django.shortcuts import render, redirect, HttpResponse
from .models import Todo
from .forms import TodoForm


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    print(todos)

    return render(request, "todos/list.html", {"todos": todos})


def todo_delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        print(todo)
        todo.delete()
        return HttpResponse(f"刪除成功: {id}")
    except:
        print("無ID")

    return redirect("todo-list")


def todo_create(request):
    return render(request, "todos/create.html", {"form": TodoForm()})
