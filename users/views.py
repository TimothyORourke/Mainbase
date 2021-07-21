from django.contrib.auth.decorators import login_required
from django.http.request import QueryDict
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login as user_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as user_logout
from django.core import serializers
from django.forms.models import model_to_dict

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ProfileForm

from django.contrib.auth.models import User
from posts.models import Post
from .models import Follow, Profile, UserPreferences

from blog.views import get_follow_suggestions

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

@login_required
def profile(request, user):
    user = User.objects.get(username=user)
    profile = Profile.objects.get(user=user)
    posts = Post.objects.filter(author=user).order_by('-date_posted')

    try:
        following = Follow.objects.get(follower=request.user, followee=user)
    except Follow.DoesNotExist:
        following = None

    follow_suggestions = get_follow_suggestions(request)

    # Form for updating profile attributes. ex. Profile Picture
    profile_form = None
    if user == request.user:
        profile_form = ProfileForm(initial={'bio' : profile.bio})

        if request.POST:
            temp = ProfileForm(request.POST, request.FILES)
            if temp.is_valid():
                if temp.files.get('profile_pic'):
                    profile.profile_pic = temp.files['profile_pic']
                if temp.files.get('profile_banner'):
                    profile.profile_banner = temp.files['profile_banner']

                profile.bio = temp.cleaned_data['bio']
                profile.save()
            else:
                profile_form = temp

    return render(request, 'users/profile.html', { 
        'profile' : profile, 'posts' : posts, 'profile_form' : profile_form,
        'follow_suggestions' : follow_suggestions, 'following' : following
        })

def resize_image(image, **kwargs):
    max_width = kwargs.get('max_width', 1080)
    pass

@login_required
def follow_api(request, username):
    followee = User.objects.get(username=username)
    if request.method == 'PUT':
        follow_obj = Follow.objects.create(follower=request.user, followee=followee)

        return JsonResponse({'follower': request.user.username, 'followee': followee.username}, status=201)

    if request.method == 'DELETE':
        follow_obj = Follow.objects.get(follower=request.user, followee=followee)
        follow_obj.delete()

        return JsonResponse({}, status=200)

    return JsonResponse({}, status=405)

@login_required
def settings_api(request):
    if request.method == 'PUT':
        darkmode = True if (QueryDict(request.body).get('darkmode') == 'true') else False
        userpreferences = UserPreferences.objects.get(user=request.user)
        userpreferences.darkmode = darkmode
        userpreferences.save()

        return JsonResponse({'user': request.user.username, 'darkmode': userpreferences.darkmode}, status=201)

    return JsonResponse({}, status=405)