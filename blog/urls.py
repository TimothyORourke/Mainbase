from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('p/<str:pk>', views.PostDetailView.as_view(), name='post-detail'),
]
