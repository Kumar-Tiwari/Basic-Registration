from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login as lgn

def Login_View(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            print('hello')
            lgn(request,user)
            return redirect('/')
        else:
            return render(request,"Login/login.html",{"form":"Error username or password"})

    else:
        return render(request,"Login/login.html",{})
