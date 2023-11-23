from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from account.models import User
from cart.models import Order, ProductsInOrder
from catalog.models import Product


def view_fav(request):
    path = request.GET.get('next')

    context = {
        'next': path,
    }

    cart = request.session.get('cart', None)

    if cart:
        products = {}
        product_list = Product.objects.filter(pk__in=cart.keys()).values('id', 'title', 'description')

        for product in product_list:
            products[str(product['id'])] = product

        for key in cart.keys():
            cart[key]['product'] = products[key]

        context['cart'] = cart

    return render(request, 'favs.html', context)