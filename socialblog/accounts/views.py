from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import aauthenticate, login , logout

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            # user.is_active = False
            user.save()
            messages.success(request, "Registration successfull. Please login!")
            return redirect('login')    
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {'form': form})

def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, "You are now logged in!")
            return redirect('dashboard')
    
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out!")
    return redirect('login')