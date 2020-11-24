from django.shortcuts import render
from .models import Post
from .forms import PostForm, FindForm
from django.utils import timezone
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .getNews import headlines

# Create your views here.
def home(request):
    posts = Post.objects.all()
    findform= FindForm()
    news = headlines['articles']

    params = {
        'findform': findform,
        'posts': posts,
        'news': news,
    }
    return render(request, 'blog/post.html', params)


@login_required(login_url='login')
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

    findform = FindForm()
    params = {
        'findform': findform,
        'form': form,
    }
    return render(request, 'blog/post_create.html', params)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    findform = FindForm()
    params = {
        'findform': findform,
        'post': post
    }
    return render(request, 'blog/post_detail.html', params)

def update(request, pk):
    post = Post.objects.get(id=pk)
    findform = FindForm()
    if(request.method == 'POST'):
        newpost = PostForm(request.POST, instance=post)
        newpost.save()
        return redirect(to='/')
    params = {
        'findform': findform,
        'post': PostForm(instance=post)
    }
    return render(request, 'blog/update.html', params)

@require_POST
def delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect(to='/')

def find(request):
    if(request.method == 'POST'):
        findform = FindForm(request.POST)
        find = request.POST['find']
        posts = Post.objects.filter(Q(title__contains=find) | Q(text__contains=find))

    else:
        findform = FindForm()
        posts = Post.objects.all()
    params = {
        'findform': findform,
        'posts': posts,
    }
    return render(request, 'blog/find.html', params)