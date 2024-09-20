from django.shortcuts import render
from shop.models import Product

def shop_views(request):
    products = Product.objects.filter( pub_status = True)
    final_price = []
    for product in products:
        final_price.append(product.price - product.discount)
        
    context ={'products': products, 'final_price': final_price}
    return render(request, 'shop/shop.html' , context)

