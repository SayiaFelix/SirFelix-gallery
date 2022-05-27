from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image, category,Location

# Create your views here.
def my_gallery(request):

    # Images = Image.show_all_photos()
    locations = Location.objects.all()
    date = dt.date.today()
    Images= Image.objects.all()
    return render(request, 'gallery.html', {"date": date, "Images": Images,"locations":locations})


def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        category = request.GET.get("search")
        searched_photos = Image.search_photo_by_category(category)
        locations = Location.objects.all()
        message = f"{category}"

        return render(request, 'search.html', {"message":message, "Images":searched_photos, "locations":locations })

    else:
        message = "You haven't searched for anything!!"
        return render(request, 'search.html', {"message":message})

