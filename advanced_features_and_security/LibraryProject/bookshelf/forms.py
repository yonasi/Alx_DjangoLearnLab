from django import forms
from .models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }





class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")

    def clean_message(self):
        message = self.cleaned_data.get('message')  # Example of additional sanitization/validation.
                                                    # Ensure that name contains only letters and spaces.
        if len(message) < 10:
            raise ValidationError("Message must be at least 10 characters long.")
        return message