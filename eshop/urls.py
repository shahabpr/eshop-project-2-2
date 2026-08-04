
from django.urls import path
from eshop import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:slug>', views.product_detail, name='product_detail')
]
