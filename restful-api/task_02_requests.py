#!/usr/bin/python3

"""
Module for fetching posts from a placeholder API and displaying or saving them.

This script provides two functions:
- `fetch_and_print_posts()` prints the HTTP status code after fetching posts.
- `fetch_and_save_posts()` saves post data (ID, title, body) to a CSV file.

Uses:
    https://jsonplaceholder.typicode.com/posts as the data source.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetches posts from a placeholder API and prints the HTTP status code."""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status code: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        for item in data:
            print(item['title'])
    else:
        print(f"Erreur: {r.status_code}")


def fetch_and_save_posts():
    """Fetches posts from a placeholder API
    and saves selected fields to a CSV file."""
    list_posts = []
    filename = 'posts.csv'

    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        data = r.json()

        for item in data:
            item = {
                "id": item['id'],
                "title": item['title'],
                "body": item['body']
            }
            list_posts.append(item)

        with open(filename, 'w', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(list_posts)

    else:
        print(f"Erreur: {r.status_code}")
