from django.db import models

class Projects(models.Model):
    project_name = models.CharField(max_length=100)


class Profile(models.Model):
    username = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    projects = models.ManyToManyField(Projects)
    profile_picture = models.ImageField(upload_to = 'images/',blank = True)