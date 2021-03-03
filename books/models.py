from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="books")
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="posts")
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="posts")
    header = models.TextField()
    body = models.TextField()
    score = models.IntegerField(default=0, blank=True)
    date = models.DateTimeField(auto_now=True, blank=True) # maybe switch auto_now back off and try and avoid the error message for timezone when creating new data

    def __str__(self):
        return f"{self.user} about {self.book} (id: {self.id})"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name="comments")
    body = models.TextField()
    score = models.IntegerField(default=0, blank=True)
    date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.user}'s comment on {self.post.user}'s post about {self.post.book.title} by {self.post.book.author.name} (id: {self.id})"