
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact-us', views.contact_page, name='contact_page'),
    path('about-us', views.about_page, name='about_page'),
    # path('site-header', views.site_header_partial, name='site_header_partial'),
]