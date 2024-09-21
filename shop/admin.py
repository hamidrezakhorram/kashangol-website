from django.contrib import admin
from shop.models import Category, Tags, Product



class ProducAdmin(admin.ModelAdmin):
   
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display = ('name' ,'pub_status','published_date','created_date' , 'price' , 'discount')
    list_filter = ('created_date', 'category' , 'tags' )
    search_fields = ['name','content']
# Register your models here.

admin.site.register(Product , ProducAdmin)
admin.site.register(Category)
admin.site.register(Tags)