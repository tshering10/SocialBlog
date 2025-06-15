from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm, ProfileForm, UserForm
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

def profile_view(request):
    profile = request.user.profile
    return render(request, "accounts/view_profile.html", {"profile": profile})

def profile_edit(request):
    user = request.user
    profile = user.profile #accessing profile from user
    
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserForm(request.POST, instance=user)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated.")    
            return redirect('profile') 
    else:
        profile_form = ProfileForm(instance=profile)
        user_form = UserForm(instance=user)
        
    context= {
        "profile_form": profile_form,
        "user_form": user_form,
    }
    return render(request, "accounts/edit_profile.html", context)