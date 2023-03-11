from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Customer, Order, OrderItems
from django.core.paginator import Paginator
from datetime import date
from django.http import HttpResponseRedirect
import json
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
    if request.method == "POST":
        print(request.POST['items'])
        customer = {
            'firstname': request.POST.get('firstname'),
            'lastname':  request.POST.get('lastname'),
            'email':  request.POST.get('email'),
            'address1': request.POST.get('address1'),
            'address2': request.POST.get('address2'),
            'city': request.POST.get('city'),
            'state': request.POST.get('state'),  
            'zip_code': request.POST.get('zip_code') 
        }

        customerObj = Customer(
            firstname=customer['firstname'],
            lastname = customer['lastname'],
            email= customer['email'],
            address1 = customer['address1'],
            address2=customer['address2'],
            city=customer['city'],
            state = customer['state'],
            zip_code = customer['zip_code']
        )
        customerObj.save()

        orderObj = Order(
            order_date = date.today(),
            customer = customerObj,
            order_total = request.POST.get('total_amount'),
            ordered_items = request.POST.get('total_items')
        )      
        orderObj.save()

        items = json.loads(request.POST['items'])
        for key,value in items.items():
            prod_id = key
            prod_qty =value[0]
            prod_name = value[1]
            prod_price = value[2]
            line_total = float(prod_price) * float(prod_qty)

            sold_product = Product.objects.get(pk=prod_id)
            orderItemsObj = OrderItems(
                order = orderObj,
                product = sold_product,
                item_qty = prod_qty,
                item_price = prod_price,
                item_amount = line_total
            )
            orderItemsObj.save()

        return HttpResponseRedirect(redirect_to="/checkout/thankyou")

    return render(request, 'shop/checkout.html')


def thankyou(request):
    return render(request, 'shop/thankyou.html')
