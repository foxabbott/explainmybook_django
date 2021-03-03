import datetime
import numpy as np
import pandas as pd
import random
import time
import string

from .models import *

BASE_PATH = r"C:/Users/JF191/explainmybook/%s.txt"

INITIAL_BOOKS_PATH = BASE_PATH % "books"
NAMES_PATH = BASE_PATH % "names"
SURNAMES_PATH = BASE_PATH % "surnames"

DEFAULT_START = datetime.datetime(year=2000, month=1, day=1)
DEFAULT_END = datetime.datetime.today()


def build_initial_books_database():

    with open(INITIAL_BOOKS_PATH, "r") as books_raw:
        lines = books_raw.readlines()
        for line in lines:
            title, author_name = line.split('\t')
            author_name = author_name.replace('\n', '')
            author = Author(name=author_name)
            author.save() # implement some method of checking for and blocking repeats
            book = Book(title=title, author=author)
            book.save()


def build_initial_user_database(num_users=10000):

    names_file = open(NAMES_PATH, "r")
    surnames_file = open(SURNAMES_PATH, "r")

    names = names_file.read().split('\n')
    surnames = [i.capitalize() for i in surnames_file.read().split('\n')]

    selected_names = random.sample(names, num_users)
    selected_surnames = random.sample(surnames, num_users)
    
    full_names = [name + " " + surname for name, surname in zip(selected_names, selected_surnames)]
    usernames = [name.lower() + surname.lower() + f"{random.randrange(10)}" for name, surname in zip(selected_names, selected_surnames)]

    count = 0
    for name, username in zip(full_names, usernames):
        password = generate_random_string(length=10)
        email = username + "@example.com"
        first_name, last_name = name.split(' ')

        user = User(first_name=first_name, last_name=last_name,
                    username=username, password=password, email=email)
        user.save()

        count += 1
        if count % 100 == 0:
            print(f"{count}/{num_users} users created.")

    names_file.close()
    surnames_file.close()


def build_initial_posts_database(average_num_posts=5, average_num_books=1, max_score=1000, min_score=-1000, start_date=DEFAULT_START, end_date=DEFAULT_END):
    all_books = [i for i in Book.objects.all()]
    all_users = [i for i in User.objects.all()]
    count = 0
    num_users = len(all_users)
    for user in all_users:
        num_posts = round(sample_from_exp_dist(mean=average_num_posts))
        num_books = min(num_posts, round(sample_from_exp_dist(mean=average_num_books)))
        if num_books != 0:

            book_list = random.sample(all_books, num_books)
            for post_num in range(num_posts):
                
                date = random_date_between(start_date, end_date)
                score = random.choice(range(min_score, max_score))
                book = random.choice(book_list)
                num_sentences = max(1, round(sample_from_exp_dist(mean=5)))
                header = generate_random_string(length=random.choice(range(15, 100)), spaces_included=True)
                body = ""
                for sentence_num in range(num_sentences):
                    body += generate_random_string(length=100, spaces_included=True) + ". "
                post = Post(user=user, book=book, body=body, header=header, date=date, score=score)
                post.save()

        count += 1
        if count % 100 == 0:
            print(f"Posts created for {count}/{num_users} users.")
    

def build_initial_comments_database(average_comments_per_post=5, max_score=100, min_score=-100, end_date=DEFAULT_END):
    all_posts = [i for i in Post.objects.all()]
    all_users = [i for i in User.objects.all()]
    count = 0
    num_posts = len(all_posts)
    print(f"Total posts: {num_posts}")
    for post in all_posts:
        num_comments = max(1, round(sample_from_exp_dist(mean=average_comments_per_post)))
        date_of_post = post.date
        if num_comments != 0:
            for comment_num in range(num_comments):

                user = random.choice(all_users)
                
                date = random_date_between(DEFAULT_START, end_date)
                # date = random_date_between(date_of_post, end_date)
                score = random.choice(range(min_score, max_score))
                num_sentences = max(1, round(sample_from_exp_dist(mean=5)))
                body = ""
                for sentence_num in range(num_sentences):
                    body += generate_random_string(length=100, spaces_included=True) + ". "
                comment = Comment(user=user, post=post, body=body, score=score, date=date)
                comment.save()
        count += 1
        if count % 100 == 0:
            print(f"Comments created on {count}/{num_posts} posts.")
            

def generate_random_string(length=100, spaces_included=False):
    if not spaces_included:
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return ''.join(random.choices(string.ascii_lowercase + string.digits + '   ', k=length))


def sample_from_exp_dist(mean):
    return np.random.exponential(scale=mean)


def random_date_between(start, end):
    return start + random.random() * (end - start)


def main():
    print("Creating books")
    build_initial_books_database()
    print("Creating users")
    build_initial_user_database()
    print("Creating posts")
    build_initial_posts_database()
    print("Creating comments")
    build_initial_comments_database()