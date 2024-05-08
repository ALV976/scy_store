from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Products


# Create your views here.
# def home(request):
# return render(request, 'home.html')

# def contacts(request):
# return render(request, 'contacts.html')

class ProductsListView(ListView):
    model = Products


class ProductsDetailView(DetailView):
    model = Products
