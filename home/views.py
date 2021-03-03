from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from books.models import Author, Book, Post


import json

BOOKS_TXT = r"books.txt"

# Create your views here.
def index_old(request):
    books = open(BOOKS_TXT, "r").read()
    title_author_pairs = books.split('\n')
    titles = [i.split('\t')[0] for i in title_author_pairs]
    # authors = [i.split('\t')[1] for i in title_author_pairs]
    # title_author = [title + ' ' + author for title, author in zip(titles, authors)]
    title_author_zipped = [i.split('\t') for i in title_author_pairs]
    # title_author_zipped = zip(titles, authors)

    return render(request, "home/home_old.html", {
        "suggestions": json.dumps(titles[:]),
    })


def index(request):
    all_books = Book.objects.all()
    books_dict = {
        book.id: {"searchable":     book.title + " " + book.author.name,
                  "title":          book.title,
                  "author":         book.author.name,
                  "list_display":   book.__str__(),
        } for book in all_books
        }
    return render(request, "home/home.html", {
        # "books": books_dict
        "books": json.dumps(books_dict)
        # "books": all_books
    })


# add a bar with login/logout etc
# eventually want people to be able to search for questions