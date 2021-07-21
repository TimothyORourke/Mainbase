from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from posts.models import Post
from posts.forms import PostForm

# Create your views here.

@login_required
def index(request):
    sort = request.GET.get('sort', 'latest')

    posts = []
    follow_suggestions = get_follow_suggestions(request)

    # Sort posts by newest by default.
    if sort == 'latest':
        posts = Post.objects.all().order_by('-date_posted')
    else:
        posts = Post.objects.all().order_by('date_posted')

    # Remove posts from accounts the user does not follow, but keep posts by self.
    for post in posts:
        if (not post.author == request.user) and (not request.user.is_following(post.author)):
            posts = posts.exclude(author=post.author)

    form = PostForm()

    if request.POST:
        temp = PostForm(request.POST)
        if temp.is_valid():
            Post.objects.create(author_id=request.user.pk, text=temp.cleaned_data['text'])
        else:
            form = temp

    return render(request, 'blog/blog.html', { 'posts' : posts, 'form' : form, 
        'follow_suggestions' : follow_suggestions })

def get_follow_suggestions(request):
    follow_suggestions = None

    # Fetch all users, excluding the current logged in user.
    follow_suggestions = User.objects.exclude(username=request.user.username)

    # Remove from the list if the current user already follows them.
    for user in follow_suggestions:
        if request.user.is_following(user):
            follow_suggestions = follow_suggestions.exclude(username=user.username)

    follow_suggestions = follow_suggestions.order_by('?')

    return follow_suggestions