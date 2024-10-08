from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name =models.CharField(max_length = 255)

    def __str__(self) -> str:
        return self.name
class Tags(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255 , null=True)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    content = models.TextField()
    pub_status = models.BooleanField(default=True)
    store_status = models.BooleanField(default=True)
    published_date = models.DateField(null=True)
    created_date = models.DateField(auto_now_add=True)
    update_date= models.DateField(auto_now=True)
    image = models.ImageField(upload_to= 'shop/' , default='shop/default.jpg')
    category =models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tags)
    counted_views = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    sell_count = models.IntegerField(default=0)
    


    def __str__(self) -> str:
        return self.name
   

class Cartitem(models.Model):
    product =models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    total_price =models.PositiveIntegerField(default=0)


    def __str__(self) -> str:
        return self.product.name


class Commentproduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateField(auto_now_add= True)
    update_date = models.DateField(auto_now=True)
    approved = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.name
