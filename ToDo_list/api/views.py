from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import List, Task
from .forms import ListForm, TaskForm


# Create your views here.
@login_required(login_url='/login/')
def main(request):
    user_name = request.user
    own_object = List.objects.filter(user = user_name).order_by('status', 'created_at')
    
    if request.method == 'POST':
        form_object = ListForm(request.POST or None)
        if form_object.is_valid():
            form_object = form_object.save(commit = False)
            form_object.user = request.user
            form_object.save()
            messages.success(request, ("New list added"))
            return redirect('main')
    else:
        form_object = ListForm()

    return render(request, "api/main.html", {"own_object" : own_object,
                                             "form_object":form_object,
                                             "user_name":user_name})

@login_required(login_url='/login/')
def singleList_view(request, list_id):
    #name = List.objects.get(id = name)
    list_object = get_object_or_404(List, id = list_id)
    
    if request.method == 'POST':
        form_object = TaskForm(request.POST or None)
        if form_object.is_valid():
            form_object = form_object.save(commit = False)
            form_object.todolist = list_object
            form_object.user = request.user
            form_object.save()
            return redirect('single-list', list_id)
    else:
        form_object = TaskForm()

    if list_object.user == request.user:
        user_lists = List.objects.filter(user = request.user).order_by('status', 'created_at')
        obj = list_object.task_set.all().order_by('Completed')
        return render(request, "api/singleList.html", {"parent_obj": list_object , "own_object" : obj, "form": form_object, "user_lists": user_lists})
    else:
        return HttpResponse("<h1>Page not available</h1> <style> h1 {color: blue;}</style>")

@login_required(login_url='/login/')
def deleteList_view(request, list_id):
    list_object = get_object_or_404(List, id = list_id)
    list_object.delete()
    return redirect('main')

@login_required(login_url='/login/')
def deleteTask_view(request, task_id, list_id):
    list_object = get_object_or_404(List, id = list_id)
    task_object = get_object_or_404(Task, id = task_id)
    task_object.delete()
    return redirect('single-list', list_id)

@login_required(login_url='/login/')
def editList_view(request, list_id):
    user_name = request.user
    list_object = get_object_or_404(List, id = list_id)
    
    form = ListForm(request.POST or None, instance = list_object)
    if form.is_valid():
        form.save()
        return redirect('main')
    else:
        return render(request, "api/editList.html", {"list_object":list_object, "user_name":user_name, "form": form})

@login_required(login_url='/login/')
def editTask_view(request, task_id, list_id):
    user_name = request.user
    list_object = get_object_or_404(List, id = list_id)
    task_object = get_object_or_404(Task, id = task_id)
    form = TaskForm(request.POST or None, instance = task_object)
    if form.is_valid():
        form.save()
        return redirect('single-list', list_id)
    else:
        return render(request, "api/editTask.html", {"task_object":task_object, "user_name":user_name, "form": form})

@login_required(login_url='/login/')
def moveTask_view(request, task_id, destinationList_id, list_id):
    task_object = get_object_or_404(Task, id = task_id)
    destination_list_object = get_object_or_404(List, id = destinationList_id)
    task_object.todolist = destination_list_object
    task_object.save()

    return redirect('single-list', list_id)
    
    