from django.urls import path
from . import views



urlpatterns = [
    path('', views.stream, name='camera'),
    path('motion/', views.motion_stream, name='motion_camera'),
]
