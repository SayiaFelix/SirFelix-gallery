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
    return render(request, 'all-images/gallery.html', {"date": date, "Images": Images,"locations":locations})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        # category = request.GET.get("search")
        # searched_photos = Image.search_photo_by_category(category)
        locations = Location.objects.all()
        # message = f"{category}"

        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"
          
        return render(request, 'search.html', {"message":message, "images":searched_images, "locations":locations })

    else:
        message = "You haven't searched for anything!!"
        return render(request, 'all-images/search.html',{"message":message})





def get_category(request, category):
    category_results = category.objects.all()
    location_results = Location.objects.all()
    category_result = Image.objects.filter(category_name__category = category)
    return render(request,'gallery.html',{'all_images':category_result,'category_results':category_results,'location_results':location_results})

def get_location(request, location):
    category_results = category.objects.all()
    locations = Location.objects.all()
    location_result = Image.objects.filter(location_name__id= location)
    return render(request,'locations.html',{'all_images':location_result,'category_results':category_results,'locations':locations})

