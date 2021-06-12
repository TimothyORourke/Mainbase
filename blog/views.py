from django.shortcuts import render
from django.views.generic import DetailView

from .models import Post

# Create your views here.

def index(request):
    sort = request.GET.get('sort', 'latest')

    if sort == 'latest':
        posts = Post.objects.all().order_by('-date_posted')
    else:
        posts = Post.objects.all().order_by('date_posted')

    return render(request, 'blog/blog.html', { 'posts' : posts })

class PostDetailView(DetailView):
    model = Post
