from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=120)

    def __str__(self):
        '''
        A string representation
        '''
        return self.location

    def save_location(self):
        '''
        A method that saves the location name
        '''
        return self.save()

    @classmethod
    def delete_location(cls, id):
        return cls.objects.filter(id = id).delete()

class category(models.Model):
    category = models.CharField(max_length=60)

    def __str__(self):
        '''
        String representation
        '''
        return self.category

    def save_category(self):
        '''
        Method to save the category name
        '''
        return self.save()


class Image(models.Model):
    '''
    A class that determines the image model characteristics
    '''
    image_name = models.CharField(max_length=30)
    image_descriptions = models.TextField()
    location_name = models.ForeignKey(Location, on_delete=models.CASCADE)
    category_name = models.ManyToManyField(category)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'photos/',null=True)

    def __str__(self):
        '''
        String representation
        '''
        return self.image_name

    def save_photo(self):
        '''
        A method that saves photo
        '''
        return self.save()

    @classmethod
    def show_all_photos(cls):
        '''
        A method that returns all photos posted in order of the most recent
        '''
        return cls.objects.order_by("post_date")[::-1]

    @classmethod
    def delete_photo(cls, id):
        '''
        A method that deletes a photo
        '''
        return cls.objects.filter(id = id).delete()

    @classmethod
    def get_photo_by_id(cls, id):
        '''
        A method to get a photo bases on the id
        '''
        return cls.objects.filter(id = id).all()

    @classmethod
    def search_photo_by_category(cls, category):
        '''
        A method to return all photos that are a specific category
        '''
        gallery = cls.objects.filter(category_name__category__icontains = category)
        return gallery

    @classmethod
    def filter_by_location(cls, search_term):
        '''
        A method to filter all photos based on a location
        '''
        locations = cls.objects.filter(location_name__location__icontains=search_term)
        return locations

