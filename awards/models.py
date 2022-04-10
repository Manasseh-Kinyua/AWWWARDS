from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images/')
    descriptioin = models.TextField(null = True)
    link = models.CharField(max_length = 2000)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    posted = models.DateTimeField(auto_now_add = True)