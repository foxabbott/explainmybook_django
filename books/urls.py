from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="booklist"),
    path("<int:book_id>/", views.book, name="book"),
    # path("<int:book_id>/<int:post_id>", views.post, name="post"),
    path("<int:book_id>/<int:post_id>/", views.post, name="post"),
    path("<int:book_id>/newpost/", views.newpost, name="newpost"),
]