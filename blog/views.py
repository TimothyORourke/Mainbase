from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from posts.models import Post
from posts.forms import PostForm

# Create your views here.

@login_required
def index(request):
    sort = request.GET.get('sort', 'latest')

    if sort == 'latest':
        posts = Post.objects.all().order_by('-date_posted')
    else:
        posts = Post.objects.all().order_by('date_posted')

    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(author_id=request.user.pk, text=form.cleaned_data['text'])
            form = PostForm(auto_id=False)
    else:
        form = PostForm(auto_id=False)

    return render(request, 'blog/blog.html', { 'posts' : posts, 'form' : form })
