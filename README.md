# Rental-property

## Create and Activate venv
- python -m venv venv
- source venv/bin/activate

## Install all requirements from requirements.txt
- pip install -r requirements.txt 

## Migrations and Running
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

## Create user admin
- python manage.py createsuperuser
- write all required fields for creating super user
- create new property (select rent or buy/sell) (photos in the end)

## Main page
- navigate to '/properties' and see all the properties (tou can search by city, postal code, location area)

## Detailed page
- If you click on view details, you can view all details

## Call page
- When click on "Call now" it would get you to call page where you need to leave your contacts

## Approved page
- Go to url "http://127.0.0.1:8000/approve_visit_requests/" and there approve or decline requests (you may check then the status in admin panel) 


## Add property page
- Go to url "http://127.0.0.1:8000/add_property" and there approve or decline requests (you may check then the status in admin panel) 
