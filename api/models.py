from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.TextField(max_length=250)
    article = models.TextField(null=True, blank=True)
    author = models.TextField(max_length=250)
    imgUrl = models.TextField(max_length=250, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
