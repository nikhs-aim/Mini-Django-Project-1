from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    p={'name':'Nikhs','college':'Pesitm','name1':'Google'}
    return render(request,'index.html',p)

def fun(request):
    return render(request,'funs.html')
