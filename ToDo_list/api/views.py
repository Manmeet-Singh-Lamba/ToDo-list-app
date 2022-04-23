from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import List, Task
from .forms import ListForm, TaskForm


# Create your views here.
def main(request):
    user_name = request.user
    own_object = List.objects.filter(user = user_name)
    
    if request.method == 'POST':
        form_object = ListForm(request.POST or None)
        if form_object.is_valid():
            form_object = form_object.save(commit = False)
            form_object.user = request.user
            form_object.save()
    else:
        form_object = ListForm()

    return render(request, "api/main.html", {"own_object" : own_object, "form_object":form_object, "user_name":user_name})
    #own_object = List.objects.get(id = 1)
    #return HttpResponse("<h1>Hello</h1> <style> h1 {color: blue;}</style>")

def singleList_view(request, list_id):
    #name = List.objects.get(id = name)
    list_object = get_object_or_404(List, id = list_id)
    user_name = request.user
    
    if request.method == 'POST':
        form_object = TaskForm(request.POST or None)
        if form_object.is_valid():
            form_object = form_object.save(commit = False)
            form_object.user = request.user
            form_object.save()
    else:
        form_object = TaskForm()

    if list_object.user == request.user:
        obj = list_object.task_set.all()
        return render(request, "api/singleList.html", {"parent_obj": list_object , "own_object" : obj, "form": form_object})
    else:
        return HttpResponse("<h1>Page not available</h1> <style> h1 {color: blue;}</style>")

def deleteList_view(request, list_id):
    list_object = get_object_or_404(List, id = list_id)
    list_object.delete()
    return redirect('main')

def deleteTask_view(request, task_id, list_id):
    list_object = get_object_or_404(List, id = list_id)
    task_object = get_object_or_404(Task, id = task_id)
    task_object.delete()
    return redirect('single-list', list_id)

def editList_view(request, list_id):
    user_name = request.user
    list_object = get_object_or_404(List, id = list_id)
    
    form = ListForm(request.POST or None, instance = list_object)
    if form.is_valid():
        form.save()
        return redirect('main')
    else:
        return render(request, "api/editList.html", {"list_object":list_object, "user_name":user_name, "form": form})
    
    