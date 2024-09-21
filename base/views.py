from .models import Post
from django.shortcuts import render

# Create your views here.


# posts = [
#     {'id':1, 'name': 'Robotics'},
#     {'id':2, 'name': 'Artifitial Intelligence'},
#     {'id':3, 'name': 'Energy'},
# ]

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'base/home.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'base/post.html', context)


def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'base/post.html', context)