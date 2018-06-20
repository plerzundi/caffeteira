from django.shortcuts import render, get_object_or_404
from .models import Post, Categoy


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})


def category(request, categoy_id):
    cat = get_object_or_404(Categoy, id=categoy_id)
    return render(request, "blog/category.html", {"category": cat})
