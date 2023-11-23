from django.db import models

from account.models import User
from catalog.models import Product


class Order(models.Model):
    customer = models.ForeignKey(User, related_name='customer',
                                 on_delete=models.CASCADE, verbose_name='Customer')
    products = models.ManyToManyField(Product, verbose_name='Products', blank=True, through='ProductsInOrder')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date and time of creation')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def str(self):
        return f'{self.customer} - {self.created}'


class ProductsInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Product', related_name='count_in_order',)
    quantity = models.PositiveSmallIntegerField(verbose_name='Quantity of goods in the order')


from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email address must be specified')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

