from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import ContactForm


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
