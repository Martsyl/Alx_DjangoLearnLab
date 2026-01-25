from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from .models import Book
from django.shortcuts import render, redirect
from .forms import BookForm
from .forms import ExampleForm

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():   # 🔐 input validation happens here
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
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
    response = render(request, 'bookshelf/book_list.html')
    response['Content-Security-Policy'] = "default-src 'self'"
    return response
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # handle form.cleaned_data here
            pass
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
Book.objects.filter(title__icontains= 'title')
