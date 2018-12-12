from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to = 'images/')  #file will go inside images subfolder inside a default media storage folder
    summary = models.CharField(max_length = 200)
