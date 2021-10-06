from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def oi(request):
    return render(request, 'modelo/index.html')