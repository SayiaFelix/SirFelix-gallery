from django.test import TestCase
from .models import Location, category, Image

# Create your tests here.
from django.test import TestCase
from .models import Location, category, Image

# Create your tests here.
class ImageTestClass(TestCase):
    '''
    Test case for the bahaviours in the image model
    '''
    # Set up method
    def setUp(self):
        # Creating a new location and saving it
        self.miami = Location(location_name='Miami')
        self.miami.save_location()

        # Creating a new category and saving it
        self.new_category = category(category_name='fun')
        self.new_category.save_category()

        self.new_image = Image(image_name = 'Miami', image_descriptions = 'Miami vibe', location = self.miami)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_method(self):
        self.new_image.save_photo()
        photos = Image.objects.all()
        self.assertTrue(len(photos) > 0)

    def test_delete_method(self):
        Image.delete_photo(self.new_image.id)
        photos = Image.objects.all()
        self.assertTrue(len(photos) == 0)

    def test_get_image_by_id(self):
        self.new_image.save_photo()
        photo = Image.get_photo_by_id(self.new_image.id)
        self.assertNotEqual(self.new_image, photo)

    def test_search_by_category(self):
        photos = Image.search_by_category("fun")
        self.assertFalse(len(photos) > 0)

    def test_filter_by_location(self):
        pass


class LocationTestClass(TestCase):
    '''
    Test case for the Location class and it's behaviours.
    '''

    # Set up method
    def setUp(self):
        '''
        Method that will run before any test case under this class
        '''
        self.new_location = Location(location_name = "Mbezi")

    def tearDown(self):
        Location.objects.all().delete()

    # Testing instance
    def test_instance(self):
        '''
        Test to confirm that the object is being instantiated correctly.
        '''
        self.assertTrue(isinstance(self.new_location, Location))


    # Testing save method
    def test_save_method(self):
        '''
        Method to check whether the locations are getting saved.
        '''
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        '''
        Method to check if we can delete a saved location
        '''
        Location.delete_location(self.new_location.id)
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_display_all(self):
        '''
        Method to check if we can display all saved locations
        '''
        miami = Location(location_name='Miami')
        miami.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations), 2)



class categoryTestClass(TestCase):
    '''
    A class that tests the category model behaviour
    '''
    def setUp(self):
        '''
        Creating a new instance
        '''
        self.category = category(category_name = 'fun')
        self.category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, category))


    def test_save_method(self):
        categories = category.objects.all()
        self.assertTrue(len(categories) > 0)