from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    re_path('^$', views.my_gallery, name='my_gallery'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'category/(\d+)', views.get_category, name = 'get_category'),
    re_path(r'location/(\d+)', views.get_location, name = 'get_location'),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
