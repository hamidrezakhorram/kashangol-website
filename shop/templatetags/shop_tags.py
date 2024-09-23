from django import template
from shop.models import Product , Category

register = template.Library()

@register.inclusion_tag('shop/shop-discount.html')
def discount_tag(arg = 3):
    products = Product.objects.filter(pub_status=1).exclude(discount =0).order_by('price')[:arg]
    for product in products:
        product.price = product.price - product.discount
    return {'products': products}
    
    
       


@register.inclusion_tag('shop/shop-categories.html')
def shopcategory():
    products = Product.objects.filter(pub_status=1)
    categories = Category.objects.all()
    catdict ={}
    for name in categories:
        catdict[name]=products.filter(category = name).count()
    return {'categories': catdict}   


# @register.inclusion_tag('shop/shop-filter.html')
# def shopfilter(request):
#     sort_options =request.GET.get('sort','')
#     products = Product.objects.filter(pub_status=1)
#     if sort_options == 'popularity': 
#         products = products.order_by('-rating')
#     elif sort_options == 'price':
#         products = products.order_by('price')
#     elif sort_options == 'discount':
#         products = products.order_by('-discount')
#     return {'products' : products}    
    

    