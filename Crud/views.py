from django.forms import models
from django.shortcuts import render
from django.template import context
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bookes

# Create your views here.
class AddBook(CreateView):
    model = Bookes
    fields = ['name', 'Author', 'Price','description']
    template_name = 'Crud/add_Bookes.html'
    success_url = '/Crud/view'

class ViewBook(ListView):
    model = Bookes
    Books = model.objects.all()
    context_object_name = 'Books'
    template_name = 'Crud/view_Book.html'    

class DetailBook(DetailView):
    model = Bookes
    context_object_name = 'Books'
    template_name = 'Crud/detail_book.html'

class DeleteBook(DeleteView):
    model = Bookes
    template_name = "Crud/delete.html"
    success_url = '/Crud/view'


class UpdateBook(UpdateView):
    model = Bookes
    fields = ['name', 'Author', 'Price','description']
    template_name = 'Crud/update_book.html'
    success_url = '/Crud/view'

        

        
