from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



def index(request):
    return render(request, 'index.html')


def register_page(request):
    form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request, 'assets/signup.html', context)