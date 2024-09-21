from django import template
from shop.models import Product

register = template.Library()

@register.inclusion_tag('shop/shop-discount.html')
def discount_tag(arg = 3):
    products = Product.objects.filter(pub_status=1).exclude(discount =0).order_by('price')[:arg]
    for product in products:
        product.price = product.price - product.discount
    return {'products': products}
    
    
       


# @register.inclusion_tag('shop/shop-discount.html')
# def postcategory():
#     products = Product.objects.filter(pub_status=1)
#     categories = Category.objects.all()
#     catdict ={}
#     for name in categories:
#         catdict[name]=posts.filter(Category = name).count()
#     return {'categories': catdict}   
