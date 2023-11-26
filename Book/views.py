from django.shortcuts import render, HttpResponse, redirect
from Book.forms import BookForm
from django.contrib import messages
from Book.models import Book

# Create your views here.
def index(request):
  context = {}
  context['books'] = Book.objects.all()
  return render(request, 'index.html', context)

def display(request):
  return HttpResponse("Book list displayed")

def submit(request):
  context = {}
  form = BookForm()
  context['form'] = form

  if request.method == "POST":
    form = BookForm(request.POST)
    form.save()
    messages.success(request, 'Book entry done successfully!!')
    return redirect('/')

  return render(request, 'submit.html', context)