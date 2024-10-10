from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_views , name ='index'),
    
   
    path('about' , about_views , name ='about'),
    path('contact' ,contact_views , name ='contact'),
    
    path('questions' ,questions_views , name ='questions'),
    path('terms' ,terms_views , name ='terms'),
    path('retunpolicy' ,return_views , name ='return'),
    path('newsletter' ,newsletter_views , name ='newsletter'),


    
]