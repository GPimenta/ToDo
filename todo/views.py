from django.contrib import messages
from django.shortcuts import render, redirect

from .models import ToDo
from .forms import TodoForm


# Create your views here.

def index(request):
    item_list = ToDo.objects.order_by("-date")

    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('ToDo')

    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }

    return render(request, 'todo/index.html', page)


def remove(request, item_id):
    item = ToDo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')