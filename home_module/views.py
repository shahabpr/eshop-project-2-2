from django.shortcuts import render


def home_page(request):
    return render(request, 'home_module/home_page.html')

def about_page(request):
    return render(request, 'home_module/about_page.html')

def contact_page(request):
    return render(request, 'home_module/contact_page.html')

def site_header_component(request):
    context = {
        'link': 'آموزش جنگو'
    }
    return render(request, 'shared/site_header_component.html', context)

def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html')