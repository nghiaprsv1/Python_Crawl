from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from .models import *
from django.views import View
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def home(request):
    products= Product.objects.all()
    context={'products':products}
    return render(request,"crawl/home.html",context)

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

bieudosanpham