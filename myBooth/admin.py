from django.contrib import admin
from .models import Location,category,Image

admin.site.register(Location)
admin.site.register(category)
# admin.site.register(Image)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields=('image_name','image','post_date','category','location','image_descriptions')
    list_display = ('image_name','location','image')
    list_filter = ('post_date','category',)
    search_fields = ('location',)
    ordering = ('post_date',)

