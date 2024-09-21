from django.shortcuts import render , get_object_or_404
from shop.models import Product

def shop_views(request):
    products = Product.objects.filter( pub_status = True)
   
    for product in products:
       product.price = product.price - product.discount
        
    context ={'products': products}
    return render(request, 'shop/shop.html' , context)


def singel_views(request , pid):
    products=get_object_or_404(Product , pk = pid , pub_status = 1)
    context={'products': products} 
    return render(request, 'shop/shop-detail.html' , context)