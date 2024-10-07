from django.shortcuts import render
from .models import Post
# Create your views here.

def articles_views(request):
    posts = Post.objects.filter(pub_status=True).order_by('published_date')
    context = {'posts': posts}

    return render(request, 'articles/article.html' , context)



def single_views(request):
    return render(request, 'articles/article-single.html')
    