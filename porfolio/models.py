from django.db import models
from django.db.models import CharField, ImageField, URLField


# Create your models here.


class Project(models.Model):
    title = CharField(max_length=200)
    description = CharField(max_length=200)
    image = ImageField(upload_to="porfolio/images")
    url = URLField(blank=True)

 
