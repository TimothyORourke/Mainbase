from django.shortcuts import render

from .models import Post

# Create your views here.

def index(request):
    sort = request.GET.get('sort', 'latest')

    if sort == 'latest':
        posts = Post.objects.all().order_by('-date_posted')
    else:
        posts = Post.objects.all().order_by('date_posted')

    return render(request, 'blog/base.html', { 'posts' : posts })
