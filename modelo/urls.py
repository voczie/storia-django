from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# URLConf
urlpatterns = [
    path('submit/', views.oi)
]