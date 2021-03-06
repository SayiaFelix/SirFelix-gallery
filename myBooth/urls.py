from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  

    re_path('^$', views.main, name='main'),
    re_path('home/', views.my_gallery, name='my_gallery'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'location/(\d+)', views.get_location, name = 'get_location'),
    re_path(r'delete/(\d+)', views.delete_image, name = 'delete_image'),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
