from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library

def list_all_books(request):

    books = Book.objects.select_related('author').all()
    
    
    book_list = []
    for book in books:
        book_list.append(f"{book.title} by {book.author.name}")
    
    
    response_text = "\n".join(book_list)
    
    
    return HttpResponse(response_text, content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context
