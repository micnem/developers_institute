from django.shortcuts import render, redirect
from django.core.exceptions import *
from .forms import TodoForm, MarkCompleteForm
from .models import Todo

# Create your views here.
def display_todos(request):
    to_do_list = Todo.objects.filter(has_been_done=False)
    html =  render(request, 'display.html', {'to_do_list' : to_do_list})
    return html

def add_task(request):

    form = TodoForm()
    
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('display')
    return render(request, 'add_task.html', {'form':form})

def display_task(request, id):
    try:
        task = Todo.objects.get(id=id)
        
        return render(request, 'task.html', {'task':task})
    
    except ObjectDoesNotExist:
        return render(request, '404page.html')

def display_by_category(request, id):
    items_by_category = Todo.objects.filter(category = id)
    # items_by_category.category.all()
    return render(request, 'category.html', {'items_by_category':items_by_category})

def mark_as_complete(request, id):
    form = Todo.objects.filter(id=id).update(has_been_done=True)
    return redirect('display')