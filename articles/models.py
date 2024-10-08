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


class Commentpost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateField(auto_now_add= True)
    update_date = models.DateField(auto_now=True)
    approved = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.name
