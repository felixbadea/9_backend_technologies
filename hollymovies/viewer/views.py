from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('Hello, hello, world!')

def hello(request, var):
    return HttpResponse('Hello, hello,{var} world!')
"""
def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} world!')
"""