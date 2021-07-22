from django.http.response import HttpResponseRedirect
from django.views.generic import DetailView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from posts.forms import PostForm
from .models import Post

from blog.views import get_follow_suggestions

# Create your views here.

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['follow_suggestions'] = get_follow_suggestions(self.request)
        return context

@login_required
def delete(request, pk):
    if request.method == 'DELETE':
        post = Post.objects.get(pk=pk)
        if post.author == request.user:
            post.delete()
            return JsonResponse({'message': 'Post successfully deleted.'})
            
    return JsonResponse({}, status=403)

@login_required
def post_api(request):
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(author_id=request.user.pk, text=form.cleaned_data['text'])

    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)