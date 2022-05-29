# SirFelix-gallery

![SirFelix-gallery](/media/images/booth.png)

## Built By [SayiaFelix](https://github.com/SayiaFelix/)

## Description
This application allows users to view photos which i have posted and the user is able to search photos by category i.e (Studies,Studio Session,Vacation,Hike,Fun and Travel).The user will view image details and location by hovering on the photo and the admin is the only one responsible for uploading, editing or deleting photos.

## User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* View all images submitted.
* Hover on images to display more details.
* Search for images by category (Studies,Studio Session,Vacation,Hike,Fun and Travel).
* Copy links to images to share with their friends and family members.

## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the Booth
* Create new images for showcasing
* Delete images
* Update image post details.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display all images | **Home page** | Hover on the image to view image details |
| Display single images when click zoom image button| **On  click** | Image should be viewed|
| To add an image  | **Through Admin dashboard** | Add and add categories and tag location of Image|
| To edit image  | **Through Admin dashboard** | Redirected to the  image form details and editing happens|
| To delete an image  | **Through Admin dashboard ** | click on image object and confirm by delete button|
| To search  | **Enter text in search bar** | User search by category only|
| To filter by Location  | **Click drop-down on navbar** | Users can view image by Location|


## SetUp / Installation Requirements
### Prerequisites
* python3.9
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/SayiaFelix/SirFelix-gallery.git
        $ cd SirFelix-gallery

## Running the Application
* Creating the virtual environment

        $ python3.9 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.9 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.9 manage.py test myBooth

## Technologies Used
* Python3.9
* Django and postgresql

## License

Copyright (c) SayiaFelix @2022

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.