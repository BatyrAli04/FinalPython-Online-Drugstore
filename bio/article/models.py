from django.db import models

from catalog.models import Product


class Article(models.Model):
    name = models.CharField(max_length=128, verbose_name='Header')
    text = models.TextField(verbose_name='Main text')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    products = models.ManyToManyField(Product, verbose_name='Goods', blank=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.name
