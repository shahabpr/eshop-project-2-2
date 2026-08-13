from django.shortcuts import render, get_object_or_404
from eshop.models import Product


def product_list(request):
    products = Product.objects.all()

    return render(request, 'eshop/product_list.html', {
        'products': products,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'eshop/product_detail.html', {
        'product': product,
    })