from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import ContactForm, PostForm


def post_list(request):
    posts = Post.objects.filter(is_published=False).order_by("-created")
    context = {"posts": posts}
    return render(request, "blog/index.html", context)


def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/details.html", {"post": post})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            # create contsct model and save data  in db
            return redirect("blog:home")
    else:

        form = ContactForm()
    return render(request, "blog/contact.html", {"form": form})


def create_post(request):
    if request.method == "POST":
        post_form = PostForm(
            request.POST,
            request.FILES,
        )
        if post_form.is_valid():

            post = post_form.save(commit=False)
            post.author = request.user
            post.save()

            # title = post_form.cleaned_data["title"]
            # content = post_form.cleaned_data["content"]
            # price = post_form.cleaned_data["price"]
            # post = Post(title=title, content=content, price=price)
            # post.save()
            return redirect("blog:home")

    else:
        post_form = PostForm()
    return render(request, "blog/post_form.html", {"form": post_form})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:post_details", id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form})
