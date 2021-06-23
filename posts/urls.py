from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('<str:pk>', login_required(views.PostDetailView.as_view()), name='post-detail'),
]
