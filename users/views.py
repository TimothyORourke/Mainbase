from users.models import Profile
from django.contrib.auth.models import User
from posts.models import Post
from django.contrib.auth import authenticate
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as user_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as user_logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'users/signup.html', { 'form' : form })

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect('index')

    form = AuthenticationForm()
    return render(request, 'users/login.html', { 'form' : form })

def logout(request):
    user_logout(request)
    return redirect('index')

def profile(request, user):
    user = User.objects.get(username=user)
    profile = Profile.objects.get(user=user)
    posts = Post.objects.filter(author=user).order_by('-date_posted')
    return render(request, 'users/profile.html', { 'profile' : profile, 'posts' : posts })
