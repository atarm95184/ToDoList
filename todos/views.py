from django.shortcuts import render, redirect, HttpResponse
from .models import Todo
from .forms import TodoForm


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all().order_by("-created", "-important")
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

    if request.method == "POST":
        print(request.POST)
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            print("新增成功")
            return redirect("todo-list")  # 儲存完回首頁

    return render(request, "todos/create.html", {"form": TodoForm()})
