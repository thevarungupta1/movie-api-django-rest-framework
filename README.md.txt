# Create a Virtual Environment

> python -m venv <virtual_env_name>

> <virtual_env_name>\Scripts\activate


Demo
----
G:\Project\django\rest-api-project>python -m venv menv

G:\Project\django\rest-api-project>menv\Scripts\activate

(menv) G:\Project\django\rest-api-project>

> pip freeze

> pip install Django

> pip freeze

> python -m pip install --upgrade pip    // optional

> django-admin startproject watchmate

> python manage.py migrate

> python manage.py createsuperuser


# create model
watchlist_app/model.py

'......

from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

....'

> python manage.py makemigrations

> python manage.py migrate

> python manage.py runserver


# register model
watchlist_app/admin.py


from django.contrib import admin
from watchlist_app.models import Movie

# Register your models here.
admin.site.register(Movie)


