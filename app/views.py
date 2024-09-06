from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page or another page after successful registration
    context = {"form": form}
    return render(request, 'assets/signup.html', context)



def login_page(request):
    return render(request, 'assets/login.html')