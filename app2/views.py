from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse


# Create your views here.
from.forms import CustomUser1
def Cust(req):
    if req.method =='POST':
        form=CustomUser1(req.POST)
        if form.is_valid():
            form.save()
            return redirect('x')
    else:
        form=CustomUser1()
    return render(req,'register.html',{'formm':form})

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def user_login(req):
    if req.method == 'POST':
        username=req.POST.get('name')
        password=req.POST.get('password')
        user=authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect('admindash')
        else:
            messages.error(req,'invalid username')
    return render(req,'login.html')
@login_required
def home(req):
    return render(req,'home.html')
def user_logout(req):
    logout(req)
    messages.info(req,"You have been loggedout")
    return redirect('x')
@permission_required('app2.can_view_protected_page')
def protected_view(req):
    return render(req,'protected.html',{'user':req.user})
def logsession(req):
    if req.method == 'POST':
        user_name=req.POST.get('name')
        password=req.POST.get('password')
        user=usermodel.objects.filter(user_name=user_name,password=password).first()
        if user is not None:
            req.session['user_id']=user.user_id
            req.session['user_name']=user.user_name
            return redirect('home')
        else:
            return render(req,'login2.html')
    else:
        return render(req,'login2.html')
    
def loginsession(req):
    if req.method == 'POST':
        name=req.POST.get('name')
        password=req.POST.get('password')
        user=newuser.objects.filter(usern_name=name,passwordn=password).first()
        if user is not None:
            req.session['user_id']=user.usern_id
            return redirect('home')
        else:
            return render(req,'login2.html')
    else:
        return render(req,'login2.html')
def homesession(req):
    return render(req,"homesession.html")

@login_required
def dashboard(req):
    if req.user.groups.filter(name='admin').exists():
        val="Admin"
        return render(req,"admin_dashboard.html",{'name':val})
    elif req.user.groups.filter(name='staff').exists():
        val="Staff"
        return render(req,"admin_dashboard.html",{'name':val})
    elif req.user.groups.filter(name='customer').exists():
        val="Customer"
        return render(req,"admin_dashboard.html",{'name':val})
    else:
        return HttpResponse("you don't have permission to this page")
