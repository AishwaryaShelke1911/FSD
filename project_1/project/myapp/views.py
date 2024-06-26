from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm

def login_action(request):
    global email, password
    if request.method == "POST":
        d = request.POST
        for key,value in d.items():
            if key == "email":
                emial = value
                if key == "password":
                    password = value
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your data got saved!")
        else:
            return HttpResponse("Failed to save data!")
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})        