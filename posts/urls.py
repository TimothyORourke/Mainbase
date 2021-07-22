from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.post_api, name='post-api'),
    path('<str:pk>/delete', login_required(views.delete), name='post-delete'),
    path('<str:pk>', login_required(views.PostDetailView.as_view()), name='post-detail'),
]
