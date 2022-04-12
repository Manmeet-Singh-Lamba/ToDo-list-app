from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import List
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

def singleList_view(request, name):
    #name = List.objects.get(id = name)
    name = get_object_or_404(List, id = name)
    if name.user == request.user:
        obj = name.task_set.all()
        return render(request, "api/singleList.html", {"parent_obj": name , "own_object" : obj})
    else:
        return HttpResponse("<h1>Page not available</h1> <style> h1 {color: blue;}</style>")

def login(request):
    return render(request, "api/login.html", {})
    