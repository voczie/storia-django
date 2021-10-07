from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# URLConf
urlpatterns = [
    path('index/', views.submit_form, name='index'),
    path('submit/', views.submit_form, name='submit'),
    path('members/', views.members, name='members'),
    path('social/', views.social, name='social')
]