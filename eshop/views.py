from django.shortcuts import render, get_object_or_404
from eshop.models import Product


def product_list(request):
    products = Product.objects.all().order_by('-id')[:6]
    return render(request, 'eshop/product_list.html', {
        'products': products,
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