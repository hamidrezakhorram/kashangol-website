from django.shortcuts import render
from shop.models import Category , Product


# Create your views here.

def index_views(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    products_by_category = {category: Product.objects.filter(category__in=[category]) for category in categories}  

    context = {'categories': categories , 'products': products , 'products_by_category': products_by_category}

    return render(request, 'index.html' , context)




def articles_views(request):
    return render(request, 'articles/article.html')

def about_views(request):
    return render(request, 'about.html')

def contact_views(request):
    return render(request, 'contact.html')

def cart_views(request):
    return render(request, 'shop/cart.html')
def questions_views(request):
    return render(request, 'F&Q.html')
def terms_views(request):
    return render(request, 'termusage.html')

