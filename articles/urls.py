from django.urls import path
from .views import *
app_name= 'articles'

urlpatterns = [
    path('' ,articles_views , name ='index'),
    path('/<int:pid>', single_views , name ='single'),


    
]