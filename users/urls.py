from django.urls import path

from . import views

urlpatterns = [
    path('follow/<str:username>', views.follow_api, name='follow-api'),
    path('settings/', views.settings_api),
]
