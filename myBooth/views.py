from django.shortcuts import render

# Create your views here.
def my_gallery(request):
    
    return render(request, 'gallery.html')
