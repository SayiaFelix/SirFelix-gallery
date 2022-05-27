from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image, category,Location

# Create your views here.
def my_gallery(request):

    Images = Image.show_all_photos()
    locations = Location.objects.all()
    date = dt.date.today()
    # Images= Image.objects.all()
    return render(request, 'gallery.html', {"date": date, "Images": Images,"locations":locations})



