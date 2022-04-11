from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images/')
    descriptioin = models.TextField(null = True)
    profile = models.ForeignKey("Profile", on_delete = models.CASCADE, null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    link = models.CharField(max_length = 2000)
    location = models.CharField(max_length = 100, null = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    posted = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_projects(cls):
        return cls.objects.all()

    def save_project(self):
        self.save()

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/')
    bio = models.TextField(null=True)
    phone_no = models.IntegerField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.bio