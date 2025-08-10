from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User



class Notebook(models.Model):
    brand = models.CharField(max_length=100)
    pages = models.IntegerField()
    size = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default="No description available")
  # Long explanation about the book
    story = models.TextField()        # Detailed notes/story
    author = models.CharField(max_length=100, default='Unknown')
    cover_image = models.ImageField(upload_to='notebook_images/', blank=True, null=True)  # NEW FIELD

    def __str__(self):
        return self.brand
admin.site.register(Notebook)    
