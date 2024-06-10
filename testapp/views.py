from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from testapp.models import Recipes

# Create your views here.

def register_page(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        if User.objects.filter(username=username).exists():
            print('USer already Exists')
            return redirect('register')

        user=User.objects.create(username=username)
        user.set_password(password)
        user.save()  
        return redirect('login')
    return render(request,'register.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('recipes')
        else:
            return redirect('login')
    return render(request,'login.html')

@login_required(login_url='login')
def recipes_page(request):
    if request.method=='POST':
        title=request.POST.get('recipe_name')
        desc=request.POST.get('recipe_desc')
        filepath=request.FILES.get('recipe_image')
        print(filepath)

        recipes=Recipes(recipe_name=title,
                        recipe_desc=desc,
                        recipe_image=filepath)
        recipes.save()
    data=Recipes.objects.all()
    return render(request,'recipes.html',{'datas':data})
    

def logout_page(request):
    logout(request)
    return redirect('login')

def recipes_delete(request,pk):
    Recipes.objects.get(id=pk).delete()
    return redirect('recipes')





