from django.shortcuts import render , get_object_or_404
from .models import Post
# Create your views here.

def articles_views(request):
    posts = Post.objects.filter(pub_status=True).order_by('published_date')
    context = {'posts': posts}

    return render(request, 'articles/article.html' , context)



def single_views(request , pid):
    posts = get_object_or_404(Post , pk=pid  , pub_status=True)
    context = {'post': posts}
    return render(request, 'articles/article-single.html' , context)
    