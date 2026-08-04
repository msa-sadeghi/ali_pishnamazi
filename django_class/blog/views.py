from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def post_list(request):
    posts = Post.objects.filter(is_published=False).order_by("-created")
    context = {"posts": posts}
    return render(request, "blog/index.html", context)


def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/details.html", {"post": post})
