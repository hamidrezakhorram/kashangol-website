from django.urls import path
from shop.views import *

app_name = 'shop'

urlpatterns = [
    path('', shop_views , name ='shop'),
    path('/<int:pid>',singel_views , name ='single'),
    path('/search' , search_views , name ='search'),
    path('/cart', cart_views, name='view_cart'),
    path('/add/<int:product_id>/', add_to_cart_views, name='add_to_cart'),
    path('/remove/<int:item_id>/', remove_from_cart_views, name='remove_from_cart'),
    
    

    
]