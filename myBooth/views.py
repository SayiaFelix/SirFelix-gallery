from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image
# Create your views here.
def my_gallery(request):

    date = dt.date.today()
    Images= Image.objects.all()
    return render(request, 'gallery.html', {"date": date, "Images": Images})
