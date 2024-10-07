from django.db import models

# Create your models here.
class Post(models.Model):
    title =models.CharField(max_length=255)
    text= models.TextField()
    image =models.ImageField(upload_to ='aricles/' , default ='shop/default.jpg')
    counted_views = models.IntegerField(default =0)
    rating = models.IntegerField(default =0)
    pub_status =  models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    published_date = models.DateField(null = True)


    def __str__(self) -> str:
        return self.title
