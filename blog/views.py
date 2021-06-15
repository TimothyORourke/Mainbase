from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from .models import Post
from django.forms.models import model_to_dict

# Create your views here.

@login_required
def index(request):
    sort = request.GET.get('sort', 'latest')

    if sort == 'latest':
        posts = Post.objects.all().order_by('-date_posted')
    else:
        posts = Post.objects.all().order_by('date_posted')

    return render(request, 'blog/blog.html', { 'posts' : posts })

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ('text',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return JsonResponse({ 'post' : model_to_dict(post) })
