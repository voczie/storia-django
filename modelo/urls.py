from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# URLConf
urlpatterns = [
    path('index/', views.submit_form, name='index'),
    path('submit/', views.submit_form, name='submit'),
    path('save/', views.save_form, name='save'),
    path('members/', views.members, name='members'),
    path('social/', views.social, name='social')
]