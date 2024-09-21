from django.shortcuts import render , get_object_or_404
from shop.models import Product ,Category
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

def shop_views(request):
    products = Product.objects.filter( pub_status = True)
    category= Category.objects.all()
    for product in products:
       product.price = product.price - product.discount
    products=Paginator(products, 9) 
    try:
        page_number = request.GET.get("page")
        products = products.page(page_number)
    except PageNotAnInteger:
        products = products.page(1)
    except EmptyPage :
        products = products.page(1)    
    context ={'products': products , 'category': category}
    return render(request, 'shop/shop.html' , context)


def singel_views(request , pid):
    products=get_object_or_404(Product , pk = pid , pub_status = 1)
    context={'products': products} 
    return render(request, 'shop/shop-detail.html' , context)