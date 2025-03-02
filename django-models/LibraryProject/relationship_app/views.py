from . models import Library
from . models import Book
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books}) 

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html' 
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all() 
        return context
    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, role='Member')
            login(request, user)
            return redirect('list_books')
    
    else: 
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form' : form})
    


def is_admin(user):
    try:
        return user.userprofile.role == 'Admin'
    except UserProfile.DoesNotExist:
        return False

def is_librarian(user):
    try:
        return user.userprofile.role == 'Librarian'
    except UserProfile.DoesNotExist:
        return False

def is_member(user):
    try:
        return user.userprofile.role == 'Member'
    except UserProfile.DoesNotExist:
        return False



@login_required
@user_passes_test(is_admin)
def Admin(request):
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(is_librarian)
def Librarian(request):
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(is_member)
def Member(request):
    return render(request, 'member_view.html')




@user_passes_test(is_admin, login_url='/login/') 
def Admin(request):
    
    context = {
        'message': "Welcome to the admin view!"
    }
    return render(request, 'admin_view.html', context)

user_passes_test(is_librarian, login_url='/login/') 
def Librarian(request):
    
    context = {
        'message': "Welcome to the librarian view!"
    }
    return render(request, 'librarian_view.html', context)

user_passes_test(is_member, login_url='/login/') 
def Member(request):
    
    context = {
        'message': "Welcome to the member view!"
    }
    return render(request, 'member_view.html', context)



@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')

        if not title or not author:
            return HttpResponseBadRequest("Missing title or author")

        Book.objects.create(title=title, author=author)
        return redirect('list_books') 

    return render(request, 'book_add.html') 


@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')

        if not title or not author:
            return HttpResponseBadRequest("Missing title or author")

        book.title = title
        book.author = author
        book.save()
        return redirect('book_detail', pk=book.pk)

    return render(request, 'book_edit.html', {'book': book}) 


@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'book_confirm_delete.html', {'book': book})




