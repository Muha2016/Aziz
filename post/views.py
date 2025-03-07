from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def home(request):
    return redirect('threads')

def threads(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('threads')
    else:
        form = ThreadForm()
    threads = Thread.objects.all()
    return render(request, 'threads.html', {'threads': threads, 'form': form})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=id)
    else:
        form = PostForm()
    posts = Post.objects.filter(thread=thread)
    return render(request, 'thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})

def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('threads')

def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=id)
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'thread_edit.html', {'form': form, 'thread': thread})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form, 'post': post})
def threads(request):
    # ...
    return render(request, 'post/threads.html', {'threads': threads, 'form': form})
from django.shortcuts import render, redirect
from .models import Thread
from .forms import ThreadForm

from django.shortcuts import render, redirect
from .models import Thread
from .forms import ThreadForm

def threads(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('threads')
    else:
        form = ThreadForm()  # Вот куда нужно вставить 2 пункт
    threads = Thread.objects.all()
    return render(request, 'post/threads.html', {'threads': threads, 'form': form})