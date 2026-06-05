from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=75)
  body = models.TextField() #relates to text form area
  slug = models.SlugField()
  date = models.DateTimeField(auto_now_add=True) #date timestamp added every time a post is made.