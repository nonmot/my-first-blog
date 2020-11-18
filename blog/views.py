from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    params = {
        'posts': posts
    }
    return render(request, 'blog/post.html', params)