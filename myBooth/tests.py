from django.test import TestCase
from .models import Location, category, Image

# Create your tests here.
class LocationTestClass(TestCase):
    '''
    Test case for the Location class and it's behaviours.
    '''
    # Set up method
    def setUp(self):
        '''
        Method that will run before any test case under this class
        '''
        self.new_location = Location(location = "Mbezi")

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
        mombasa = Location(location='Mombasa')
        mombasa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations), 2)

