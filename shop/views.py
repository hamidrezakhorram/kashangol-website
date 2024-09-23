from django.shortcuts import render , get_object_or_404
from shop.models import Product ,Category
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.db.models import Max

def shop_views(request):
    sort_options =request.GET.get('sort','')
    price_range = request.GET.get('price_range',0)  
    products = Product.objects.filter( pub_status = True)
    category= Category.objects.all()
    for product in products:
       product.price = product.price - product.discount  

    # sort by price , rating and discount
    if sort_options:
       if sort_options == 'popularity"': 
        products = products.order_by('-rating')
       elif sort_options == 'price':
        products = products.order_by('price')
       elif sort_options == 'discount':
         products = products.order_by('-discount')
    
    #price range filter
    max_price = Product.objects.aggregate(Max('price'))['price__max']

    if price_range:
        price_range = int(price_range)
        products = products.filter(price__lte = price_range)


    # paginate          
    products=Paginator(products, 9) 
    try:
        page_number = request.GET.get("page")
        products = products.page(page_number)
    except PageNotAnInteger:
        products = products.page(1)
    except EmptyPage :
        products = products.page(1)

    context ={'products': products , 
              'category': category ,
              'sort_option': sort_options, 
              'price_range' :price_range ,
              'max_price' : max_price, 
              }
    return render(request, 'shop/shop.html' , context)



def singel_views(request , pid):
    products=get_object_or_404(Product , pk = pid , pub_status = 1)
    context={'products': products} 
    return render(request, 'shop/shop-detail.html' , context)

def discount_views(request):
    products= Product.objects.filter( pub_status = True)
    products_max = products.objects.order_by('-price')
    context={'products_max': products_max}
    
   

    return render(request, 'shop/shop-discount.html'  , context)        

    
def search_views(request):
    products =Product.objects.filter(pub_status=1)  # Filter only active posts
    query = request.GET.get('s')  # Get search query
    if query:
        products = products.filter(name__icontains=query)  # Perform case-insensitive search
    context = {'products': products}
    return render(request, 'shop/shop.html', context)    