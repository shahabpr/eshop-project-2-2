from django.db import models
from django.utils.text import slugify
from django.urls import reverse



class CaptionP(models.Model):
    caption = models.CharField(max_length=200, db_index=True, verbose_name='تگ محصول')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصول'


class ProductCategory(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    title_url = models.CharField(max_length=200, db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام محصول")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت")
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    short_Description = models.CharField(max_length=300, null=True, blank=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات مفصل')
    slug = models.SlugField(default='', null=False, verbose_name='url محصول', max_length=200, unique=True)
    category = models.ManyToManyField(ProductCategory, verbose_name='دسته بندی ها', related_name='products')
    captions = models.ManyToManyField(CaptionP, verbose_name='کپشن ها', related_name='captions')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
