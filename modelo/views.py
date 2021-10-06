from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def oi(request):
    if request.method == 'GET':
      return render(request, 'modelo/index.html')
    else:
      return render(request, 'modelo/index.html')
