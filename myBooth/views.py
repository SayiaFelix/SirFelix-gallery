
from django.shortcuts import render,redirect
from django.http  import Http404
import datetime as dt
from .models import Image,Location, category

# Create your views here.
def my_gallery(request):
    Images = Image.show_all_photos()
    locations = Location.objects.all()
    date = dt.date.today()
    # Images = Image.objects.all()
    return render(request, 'all-images/gallery.html', {"date": date, "Images": Images,"locations":locations})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search-images.html',{"message":message,"Images": searched_images})

    else:
        message = "You haven't searched for any Category"
        return render(request, 'all-images/search-images.html',{"message":message})


def get_location(request, location_id ):
    try:
        image = Image.objects.get(id= location_id )
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/locations.html", {"image":image})

# def get_location(request, location_name):
#     category_results = category.objects.all()
#     locations = Location.objects.all()
#     location_result = Image.objects.filter(location__id= location_name)
#     return render(request,'all-images/locations.html',{'all_images':location_result,'category_results':category_results,'locations':locations})

def delete_image(request, image_id):
    image=Image.objects.filter(id = image_id).delete()
    
    return redirect('my_gallery')
