from . models import Library
from . models import Book
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import DetailView
from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test


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
    return user.UserProfile.role == 'Admin'


def is_librarian(user):
    return user.UserProfile.role == 'Librarian'

def is_member(user):
    return user.UserProfile.role == 'Member'


@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, 'member_view.html')






