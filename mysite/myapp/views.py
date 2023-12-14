from django.shortcuts import render, redirect
from .forms import Commentform
from .models import Post

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'myapp/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    form = Commentform()  # Initialize form outside the conditional

    if request.method == 'POST':
        form = Commentform(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)

    return render(request, 'myapp/post_detail.html', {'post': post, 'form': form})
