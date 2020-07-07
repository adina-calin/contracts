from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('acasa')

def contract(request):
    return HttpResponse('contract')

def actaditional(request):
    return HttpResponse('actaditional')

