from django.shortcuts import render , redirect
from django.contrib.auth import  authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  UserCreationForm

# Create your views here.
def login_views(request):
    form = UserCreationForm()  
    if request.method == 'POST':
        if 'login_form' in request.POST:
             print("i got this")
             username = request.POST.get('username')
             password = request.POST.get('password')
             user = authenticate(request , username = username , password = password)
             if user is not None:
                login(request , user )
                return redirect('/')
          
        
        elif 'signup_form' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            
   
           

    return render(request, 'accounts/index.html' , {'form' : form})        

                
       
@login_required
def logout_views(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')    
