from django.shortcuts import render , get_object_or_404 , redirect
from .models import *
from .forms import CommentForm
# Create your views here.

def articles_views(request):
    posts = Post.objects.filter(pub_status=True).order_by('published_date')
    context = {'posts': posts}

    return render(request, 'articles/article.html' , context)



def single_views(request , pid):
    posts = get_object_or_404(Post , pk=pid  , pub_status=True)
    comments = Commentpost.objects.filter(post=posts.id, approved=True).order_by('created_date')
    form = CommentForm()


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = posts 
            comment.approved = False 
            comment.save()
            return redirect('articles:single', pid=pid)
        else:
            print('action was unsseccessful') 


    
    context = {'post': posts , 'comments': comments , 'form': form}
    return render(request, 'articles/article-single.html' , context)
    