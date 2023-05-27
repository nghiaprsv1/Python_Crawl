from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from .models import *
from django.views import View
import json
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .import importdb
from .import drawchartcrawl
# Create your views here.
def home(request):
    products= Product.objects.all()
    context={'products':products}
    return render(request,"crawl/home.html",context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'crawl/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:messages.info(request,"User Or PassWord Not Correct!")
    context = {}
    return render(request,'crawl/login.html',context)

def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
    return render(request,"crawl/search.html",{"searched":searched, "keys": keys})

def bieudosanpham(request):
    context={}
    return render(request,"crawl/bieudosanpham.html",context)

def bieudothuonghieu(request):
    brands= Product.objects.all()
    context={'brands':brands}
    return render(request,"crawl/bieudothuonghieu.html",context)

def bieudocuahang(request):
    brands= Product.objects.all()
    context={'brands':brands}
    return render(request,"crawl/bieudocuahang.html",context)

class Category(View):
    def get(self,request,pk):
       product= Product.objects.get(pk=pk) 
       return render(request,"crawl/category.html",locals())
    
class Todo(View):
    def get(self,request,pk):
       product= Product.objects.get(pk=pk) 
       return render(request,"crawl/bieudo.html",locals())
def todo(request):
    context={}
    return render(request,"crawl/bieudo.html",context)

def import_view(request):
    if request.method == 'POST':
        file = request.FILES['file']
        importdb.import_data(file)
        # drawchartcrawl.drawchartcrawl(file)
        messages.success(request, 'Upload File Thành Công')
    return render(request,"crawl/home.html")
