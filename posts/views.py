from django.views.generic import CreateView, DetailView
from django.http import JsonResponse
from django.forms.models import model_to_dict

from django.shortcuts import render

from .models import Post

# Create your views here.

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
