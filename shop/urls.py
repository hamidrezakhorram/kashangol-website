from django.urls import path
from shop.views import *

app_name = 'shop'

urlpatterns = [
    path('', shop_views , name ='shop'),
    path('/<int:pid>',singel_views , name ='single'),
    path('/search' , search_views , name ='search'),
    

    
]