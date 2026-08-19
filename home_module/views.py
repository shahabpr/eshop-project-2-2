from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactUsForm

def home_page(request):
    return render(request, 'home_module/home_page.html')

def about_page(request):
    return render(request, 'home_module/about_page.html')


def contact_page(request):
    if request.method == 'POST':
        contactus_form = ContactUsForm(request.POST)
        if contactus_form.is_valid():
            print(contactus_form.cleaned_data)
            return redirect('home_page')

    contactus_form = ContactUsForm()
    return render(request, 'home_module/contact_page.html', {
        'contactus_form': contactus_form
    })

def site_header_component(request):
    context = {
        'link': 'آموزش جنگو'
    }
    return render(request, 'shared/site_header_component.html', context)

def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html')