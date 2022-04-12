from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form_object  = SignUpForm(request.POST or None)
        if form_object.is_valid():
            form_object.save()
    else:    
        form_object  = SignUpForm()
    return render(request, "signUp/signUp.html", {"form":form_object})