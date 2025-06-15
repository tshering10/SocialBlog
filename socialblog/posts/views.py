from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from accounts.models import Profile
from posts.forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "posts/home.html")

@login_required
def dashboard(request):
    posts = Post.objects.all().order_by('-id')
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "posts/dashboard.html", {'posts': posts, 'profile':profile})

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/post_detail.html", {'post': post})
    
def create_post_view(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "New post created!")
            return redirect("dashboard")
    else:
        form = PostForm()
    return render(request, "posts/create_post.html", {"form": form})

def edit_post_view(request , pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Your post has been updated!")
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "posts/edit_post.html", {"form": form})

def delete_post_view(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.info(request, "Your post has been deleted.")
    return redirect("dashboard")

@login_required
def activeuser_post_view(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    profile = Profile.objects.get(user=request.user)
    return render(request, "posts/user_post.html", {'posts':posts, 'profile':profile})

def about_us(request):
    return render(request, "posts/about_us.html")

def contact(request):
    return render(request, "posts/contact.html")