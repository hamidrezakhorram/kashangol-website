from django.shortcuts import render , get_object_or_404 , redirect
from shop.models import  * 
from shop.forms import CommentForm

# from shop.forms import CommentForm

from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.db.models import Max

def shop_views(request):
    sort_options =request.GET.get('sort','')
    price_range = request.GET.get('price_range',0) 
    category_id = request.GET.get('category', None) 
    products = Product.objects.filter( pub_status = True)
    category= Category.objects.all()
    for product in products:
       product.price = product.price - product.discount  
    
    if category_id:
       products = products.filter(category=category_id)

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
    products_category = products.category.all()
    products_offer =Product.objects.filter(category__in =products_category).exclude(pk= products.pk)
    comments = Commentproduct.objects.filter(product=products.id, approved=True).order_by('created_date')
    form = CommentForm()
    rating =0
    rating_count = 0
    for user in comments :
       rating = user.rating + rating
       rating_count +=1
    if rating_count != 0:
        products.rating = rating / rating_count   



    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = products  
            comment.approved = False 
            comment.rating = request.POST.get('rating')
            comment.save()
            return redirect('shop:single', pid=pid)  


    
       
    context={'products': products , 'products_offer': products_offer , 'comments': comments , 'form': form} 
    return render(request, 'shop/shop-detail.html' , context)

def discount_views(request):
    products= Product.objects.filter( pub_status = True)
    products_max = products.objects.order_by('-price')
    context={'products_max': products_max}
    
   

    return render(request, 'shop/shop-discount.html'  , context)        

    
def search_views(request):
    products =Product.objects.filter(pub_status=1)  
    query = request.GET.get('s')  
    if query:
        products = products.filter(name__icontains=query)
    context = {'products': products}
    return render(request, 'shop/shop.html', context)    


def cart_views(request):
    cart_items = Cartitem.objects.filter(user=request.user)
    
    for item in cart_items:
       item.total_price = item.product.price * item.quantity
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    total_discount = sum(item.product.discount * item.quantity for item in cart_items)
    final_price = total_price - total_discount

    context = { 'cart_items': cart_items,
                'total_price': total_price,
                'final_price': final_price,
                'total_discount': total_discount,
                
    }
    return render(request, 'shop/cart.html', context)

def add_to_cart_views(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item , create = Cartitem.objects.get_or_create(product=product,  user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:view_cart')


def remove_from_cart_views(request, item_id):
    cart_item = Cartitem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('shop:view_cart')

   
   