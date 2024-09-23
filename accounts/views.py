from django.shortcuts import render

# Create your views here.
def login_views(request):
    return render(request, 'accounts/index.html')