from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.db.models import Q

# Create your views here.

from django.http import HttpResponse

from .models import Book

def index(request):
    return HttpResponse("Hello, world. You're at the bookshelf index.")


#1. Managing Permissions and Groups in Django

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/templates/bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/templates/bookshelf/book_form.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk) # Avoid SQL injection using Django's ORM
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid(): # Data is validated and sanitized by the form, form.save()
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/templates/bookshelf/book_form.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/templates/bookshelf/book_confirm_delete.html', {'book': book})


