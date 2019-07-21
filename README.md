# Employee Manager Application

Simple Django Application to manage employees, it has an API for integration in Django Rest Framework and Django Control Panel to manage employee informations.

## Project Structure:
````
employee-manager
├── README.md
├── employee
│   ├── api
│   │	├── __init__.py
│   │	├── serializers.py
│   │	├── viewsets.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manager
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── Procfile
├── runtime.txt
├── requirements-dev.txt
└── requirements.txt
````
## Dependencies:
You need these packages to execute the project
````
Python version: 3.7.3
dj-database-url version: 0.5.0
dj-static version: 0.0.6
Django version: 2.2.3
djangorestframework version: 3.10.1
python-decouple version: 3.1
pytz version: 2019.1
sqlparse version: 0.3.0
static3 version: 0.7.0
````
## How to execute
Get the latest version from repository, in the root folder from the downloaded code, execute:


Create a python environment:
```sh
python -m venv venv
```
Activate the Python environment:
```sh
.\venv\Scripts\activate
```
Install all the dependencies:
```sh
pip install -r requirements-dev.txt
```
Make the migrations of the models
```sh
python manage.py makemigrations
```
Make the migrate to create the entities in the database (SQLite)
```sh
python manage.py migrate
```
Create the superuser to manage the admin control panel
```sh
python manage.py createsuperuser
```
Run the server, check if the port 8000 is available, if not use the port 8080.
```sh
python manage.py runserver
```
Your app should now be running on [localhost:8000](http://localhost:8000/)
