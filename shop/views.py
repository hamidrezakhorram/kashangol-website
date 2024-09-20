from django.shortcuts import render

def shop_views(request):
    return render(request, 'shop/shop.html')

