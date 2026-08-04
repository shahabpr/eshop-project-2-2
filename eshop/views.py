from django.shortcuts import render
from eshop.models import Product


def product_list(request):
    products = Product.objects.all()
    number_of_products = products.count()

    return render(request, 'product_list.html', {
        'products': products,
        'number_of_products': number_of_products,
    })



def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'product_detail.html', {
        'product': product,
    })
