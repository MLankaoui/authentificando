from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from app.forms import createUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home_page(request):
    return render(request, 'assets/home.html')

def register_page(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            # getting username
            user_name = form.cleaned_data.get('username')
            messages.success(request, f'account created with the username : {user_name}')
            return redirect('login')  # Redirect to the login page or another page after successful registration
    context = {"form": form}
    return render(request, 'assets/signup.html', context)



def login_page(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'{user_name} logged in successfully')
            return redirect('home')
        else:
            messages.warning(request, f'username or password incorrect')
    return render(request, 'assets/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')