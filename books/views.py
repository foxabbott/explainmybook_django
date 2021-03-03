from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Book, Post, User, Comment

# Create your views here.
def index(request):
    return render(request, "books/index.html", {
        "books": Book.objects.all()
    })

def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    posts = book.posts.order_by('-score') # need to add functionality for selecting by different things
    return render(request, "books/book.html", {
        "book": book,
        "posts": posts,
    })

def newpost(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(pk=book_id)
        user = User.objects.get(pk=int(request.POST["user"]))
        user.posts.add(post)

def post(request, post_id, book_id):
    post = Post.objects.get(pk=post_id)
    comments = post.comments.order_by('-score') # need to add functionality for selecting by different things
    book = post.book
    return render(request, "books/post.html", {
        "book": book,
        "post": post,
        "comments": comments,
    })


# make header dynamic: usually register, but "hello username" if logged in
# next: build form, using the video with people signing up for an account on harvard