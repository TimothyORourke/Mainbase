from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from posts.models import Post

# Create your views here.

@login_required
def index(request):
    sort = request.GET.get('sort', 'latest')

    if sort == 'latest':
        posts = Post.objects.all().order_by('-date_posted')
    else:
        posts = Post.objects.all().order_by('date_posted')

    return render(request, 'blog/blog.html', { 'posts' : posts })
