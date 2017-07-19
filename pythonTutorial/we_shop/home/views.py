# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from home.models import *
# Create your views here.

def index(request):

    categories= Categories.objects.filter();
    products = Product.objects.filter(cate_id=1)

    context ={
        'categories':categories,
        'products': products
    }

    return render(request,"home/index.html",context)

def categories (request,cate_id):
    categories = Categories.objects.filter();
    products= Product.objects.filter(cate_id=cate_id)

    context={
        'categories': categories,
        'products': products
    }
    return render(request,"home/index.html",context)