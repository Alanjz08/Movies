from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def book(request, book_id):
    context = books[book_id]
    return render(request, "book.html", context)

books = {
    1: {"titulo": "Django book example", "autor": "Juan Luis Lopez"},
    2: {"titulo": "Django book example 2", "autor": "Juan Luis Lopez"},
    3: {"titulo": "Django book example 3", "autor": "Juan Luis Lopez"},
    4: {"titulo": "Django book example 4", "autor": "Juan Luis Lopez"}

}