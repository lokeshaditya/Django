from django.urls import path
#from .views import show, about
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    #path('', show),
]