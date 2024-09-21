from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name = "home"),
    path('post/<str:pk>/', views.post, name="post"),
]