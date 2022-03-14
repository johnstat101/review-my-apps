from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=100)


class Profile(models.Model):
    username = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    projects = models.ManyToManyField(Project)
    profile_picture = models.ImageField(upload_to = 'images/', blank = True)