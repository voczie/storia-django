from django.shortcuts import render
from django.http import HttpResponse

def oi(request):
    html = "<h1>sotira djano</h1>"
    return HttpResponse(html)