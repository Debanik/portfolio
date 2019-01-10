from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
    body = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'images/')
