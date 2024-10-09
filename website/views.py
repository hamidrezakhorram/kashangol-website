from django.shortcuts import render , HttpResponseRedirect
from shop.models import Category , Product , Cartitem
from articles.models import Post

from website.forms import Newsletterform


# Create your views here.

def index_views(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    products_by_category = {category: Product.objects.filter(category__in=[category]) for category in categories}
    most_sell = Product.objects.filter(pub_status= True).exclude(sell_count = 0).order_by('-sell_count')[:6]  
    posts = Post.objects.filter(pub_status= True).order_by('-created_date')[:4]

    context = {'categories': categories ,
                'products': products ,
                'products_by_category': products_by_category,
                'most_sell' : most_sell,
                'posts' : posts


             }

    return render(request, 'index.html' , context)






def about_views(request):
    return render(request, 'about.html')

def contact_views(request):
    return render(request, 'contact.html')


def questions_views(request):
    return render(request, 'F&Q.html')
def terms_views(request):
    return render(request, 'termusage.html')


def return_views(request):
    return render (request, 'returnpolicy.html')

def newsletter_views(request):
    if request.method == 'POST':
        form = Newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')  
        else:
            print('Form is invalid!')  
           
    else:
        form = Newsletterform()  

   
    return HttpResponseRedirect('/')

    
