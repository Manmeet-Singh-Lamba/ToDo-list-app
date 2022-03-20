from django.shortcuts import render
from django.http import HttpResponse
from .models import List
from .forms import ListForm

# Create your views here.
def main(request):
    own_object = List.objects.all()
    form_object = ListForm()

    if request.method == 'POST':

        form_object = ListForm(request.POST)
        if form_object.is_valid():
            form_object.save()

    
    #own_object = List.objects.get(id = 1)
    #return HttpResponse("<h1>Hello</h1> <style> h1 {color: blue;}</style>")
    return render(request, "api/main.html", {"own_object" : own_object, "form_object":form_object})

def singleList_view(request, name):
    name = List.objects.get(id = name)
    obj = name.task_set.all()
    return render(request, "api/singleList.html", {"parent_obj": name , "own_object" : obj})


def login(request):
    return render(request, "api/login.html", {})
    