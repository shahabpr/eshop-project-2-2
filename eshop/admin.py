from django.contrib import admin
from eshop.models import Product, ProductCategory, HashtagP, ProductBrand

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name','price','is_active')
    list_filter = ('brand','categories')
    list_editable = ('is_active','price')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(HashtagP)
admin.site.register(ProductBrand)
