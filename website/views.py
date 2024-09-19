from django.shortcuts import render

# Create your views here.

def index_views(request):
    return render(request, 'index.html')


def shop_views(request):
    return render(request, 'shop/shop.html')

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

