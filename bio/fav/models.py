from django.db import models

from account.models import User
from catalog.models import Product


class Fav(models.Model):
    favs = models.ManyToManyField(Product, verbose_name='Products', blank=True, )

    class Meta:
        verbose_name = 'Favourite'
        verbose_name_plural = 'Favourites'


