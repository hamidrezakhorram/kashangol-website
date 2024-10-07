from django.shortcuts import render

# Create your views here.

def articles_views(request):
    return render(request, 'articles/article.html')



def single_views(request):
    return render(request, 'articles/article-single.html')
    