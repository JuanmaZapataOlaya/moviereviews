from django.db import models

# Create your models here.
class Movie(models.Model):
    tittle = models.CharField(max_length=100)
    description = model-CharField(max_length=250)
    image = models.imageField(upload_to ='movie/images/')
    url = models.URLField(blank=True)