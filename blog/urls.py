from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('p/create', views.PostCreateView.as_view(), name='post-create'),
    path('p/<str:pk>', login_required(views.PostDetailView.as_view()), name='post-detail'),
]
