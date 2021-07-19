from django.views.generic import DetailView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from .models import Post

# Create your views here.

class PostDetailView(DetailView):
    model = Post

@login_required
def delete(request, pk):
    if request.method == 'DELETE':
        post = Post.objects.get(pk=pk)
        if post.author == request.user:
            post.delete()
            return JsonResponse({'message': 'Post successfully deleted.'})
            
    return JsonResponse({}, status=403)
