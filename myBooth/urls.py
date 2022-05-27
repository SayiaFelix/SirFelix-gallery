from django.urls import re_path
from . import views



urlpatterns = [ 
    re_path('', views.my_gallery, name='my_gallery'),
  
]