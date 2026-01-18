from django.shortcuts import render
from django.views.generic import DetailView

from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {
        'books': books
    })


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the user immediately
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    authentication_form = AuthenticationForm

class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
