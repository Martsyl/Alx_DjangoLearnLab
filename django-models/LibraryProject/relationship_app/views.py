from django.http import HttpResponse
from django.shortcuts import render
from relationship_app.models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {
        'books': books
    })

from django.views.generic import DetailView


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
