from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('create', views.PostCreateView.as_view(), name='post-create'),
    path('<str:pk>', login_required(views.PostDetailView.as_view()), name='post-detail'),
]
