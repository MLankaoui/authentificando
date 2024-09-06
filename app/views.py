from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from app.forms import createUserForm

def register_page(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page or another page after successful registration
    context = {"form": form}
    return render(request, 'assets/signup.html', context)



def login_page(request):
    return render(request, 'assets/login.html')