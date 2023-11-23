from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):

    name = models.CharField(
        max_length=255,
        verbose_name='Category',
    )

    slug = models.SlugField(unique=True)

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Catalog',
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = ('-id',)

    class MPTTMeta:
        order_insertion_by = ['name']

    def str(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'catalog:product_list_by_category',
            kwargs={'category_slug': self.slug}
        )


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Category',
    )

    title = models.CharField(
        max_length=255,
        verbose_name='Name',
    )

    description = models.TextField(verbose_name='Description')

    image = models.ImageField(
        upload_to='catalog/',
        verbose_name='Image',
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def str(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'catalog:product_detail',
            kwargs={
                'product_slug': self.slug,
                'category_slug': self.category.slug
            }
        )


class Review(models.Model):

    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.PROTECT,
        verbose_name='Product'
    )

    name = models.CharField(
        max_length=64,
        verbose_name='Name',
    )

    rating = models.PositiveSmallIntegerField(
        verbose_name='Rating'
    )
    review = models.TextField(
        max_length=255,
        verbose_name='Feedback'
    )

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def str(self):
        return self.name