from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    products = Product.objects.all()

    search_item = request.GET.get('search_item')
    if search_item != '' and search_item is not None:
        products = products.filter(title__icontains=search_item)

    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'shop/index.html', {
        'products': products,
        'search_keyword': search_item
    })


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)

    return render(request, 'shop/product_detail.html', {
        'product': product        
    })
    
def checkout(request):
    return render(request, 'shop/checkout.html')