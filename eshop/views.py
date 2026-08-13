from django.shortcuts import render, get_object_or_404
from eshop.models import Product


def product_list(request):
    products = Product.objects.all()
    number_of_products = products.count()

    return render(request, 'eshop/product_list.html', {
        'products': products,
        'number_of_products': number_of_products,
    })


def product_detail(request, slug):
    # try:
    #     product = Product.objects.get(slug=slug)
    # except:
    #     raise Http404
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'eshop/product_detail.html', {
        'product': product,
    })