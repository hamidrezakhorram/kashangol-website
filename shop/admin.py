from django.contrib import admin
from shop.models import *
from django_summernote.admin import SummernoteModelAdmin 




class ProducAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display = ('name' ,'pub_status','published_date','created_date' , 'price' , 'discount')
    list_filter = ('created_date', 'category' , 'tags' )
    search_fields = ['name','content']
# Register your models here.

admin.site.register(Product , ProducAdmin)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Cartitem)
admin.site.register(Commentproduct)