from django import forms
from Book.models import Book

class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ['title', 'ISBN', 'publication_date']
    widgets = {
      'publication_date': forms.DateInput(attrs={'type': 'date'}),
    }