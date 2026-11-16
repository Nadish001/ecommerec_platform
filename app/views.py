from collections import Counter
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import authenticate,logout,login



def homepage(request):
    return render(request,'home1.html')

def registerpage(request):
    error={}
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if not email:
            error['msg']="All fields are required"
            return render(request,'registerpage2.html',{"error":error})
        elif password1!=password2:
            error['password']="Password does not match"
            return render(request,'registerpage2.html',{"error":error})
        else:
            user = User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            # messages.success(request,"user registered successfully ")
            return redirect(homepage)
    else:
        return render(request,'registerpage.html')


def loginpage(request):
    if request.method =='POST':
        n1=request.POST.get('n1')
        p1=request.POST.get('p1')
        # print(n1,p1)
        user = authenticate(request,username=n1,password=p1)
        if user:
            login(request,user)
            # messages.success(request,"user loggedIn successfully ")
            return redirect(homepage)
        else:
            print("invalid creditential")
    return render(request,'loginpage.html')

def logoutpage(request):
    logout(request)
    messages.success(request,"user logged out successfully ")
    return redirect(homepage)

 
def shoppage(request):
        pro = Products.objects.all()
        return render(request,'shop.html',{'pro':pro})

def addcat(request):
    if request.method =='POST':
        form = Categoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(shoppage)
    else:
        form = Categoryform()
    return render(request,'addcat.html',{'form':form})


def addproduct(request):
    if request.method =='POST':
        form = Productform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(shoppage)
    else:
        form = Productform()
    return render(request,'addpro.html',{'form':form})

def editproduct(request,pid):
    pro = Products.objects.get(id=pid)
    if request.method == 'POST':
        form = Productform(request.POST,request.FILES,instance=pro)
        if form.is_valid():
            form.save()
            return redirect(prodetails,pid)
    else:
        form = Productform(instance=pro)
    return render(request,'editpro.html',{'form':form})

def deleteproduct(request,pid):
    if request.method == 'POST':
        pro = Products.objects.get(id=pid)
        pro.delete()
        return redirect(shoppage)
    return render(request,'deletepro.html',{'pid':pid})

def prodetails(request,pid):
    po = Products.objects.get(id = pid)
    item = request.session.get('item', [])
    count = dict(Counter(item))   
    po.qty = count.get(po.id, 0)
    return render(request,"prodetails.html",{'po':po,'count':count})

def addcart(request,pid):
    pro = Products.objects.get(id=pid)
    i = request.session.get('item', [])
    i.append(pro.id)
    request.session['item'] = i
    return redirect(prodetails,pid)

def viewcart(request):
    item = request.session.get('item', [])
    count = dict(Counter(item))           
    pro = Products.objects.filter(id__in=count.keys())
    for p in pro:
        p.qty = count[p.id]               
    return render(request, "cart.html", {'pro': pro, 'count': count})
    # item = request.session.get('item')
    # pro = Products.objects.filter(id__in = item)
    # return render(request,"cart.html",{'pro':pro})

def minus(request,pid):
    i = request.session.get('item', [])
    if pid in i:
        i.remove(pid)
    request.session['item'] = i
    return redirect(viewcart)

def remove(request, pid):
    i = request.session.get('item', [])
    i = [x for x in i if x != pid]
    request.session['item'] = i
    return redirect(viewcart)

def add(request,pid):
    pro = Products.objects.get(id=pid)
    i = request.session.get('item', [])
    i.append(pro.id)
    request.session['item'] = i
    return redirect(viewcart)
def clear(request):
    i = request.session.get('item', [])
    if i:
        i.clear()
        request.session['item'] = i
    return redirect(viewcart)



