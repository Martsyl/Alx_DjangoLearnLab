from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from .models import Book
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        publication_year = request.POST['publication_year']

        Book.objects.create(
            title=title,
            author=author,
            publication_year=publication_year
        )
        return redirect('book_list')

    return render(request, 'bookshelf/create_book.html')

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.publication_year = request.POST['publication_year']
        book.save()
        return redirect('book_list')

    return render(request, 'bookshelf/edit_book.html', {'book': book})
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
