from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.
class HomeView(ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name ="products"
    #paginate_by = "1"
    