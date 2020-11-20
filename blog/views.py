from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    posts = Post.objects.all()
    params = {
        'posts': posts
    }
    return render(request, 'blog/post.html', params)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/')

    else:
        form = PostForm()
    params = {
        'form': form,
    }
    return render(request, 'blog/post_create.html', params)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    params = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', params)

def update(request, pk):
    post = Post.objects.get(id=pk)
    if(request.method == 'POST'):
        newpost = PostForm(request.POST, instance=post)
        newpost.save()
        return redirect(to='/')
    params = {
        'post': PostForm(instance=post)
    }
    return render(request, 'blog/update.html', params)

@require_POST
def delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect(to='/')