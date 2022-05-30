from turtle import title
from xml.parsers.expat import model
from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    images = models.FileField()

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    list_item1 = models.CharField(max_length=255)
    list_item2 = models.CharField(max_length=255)
    list_item3 = models.CharField(max_length=255)
    list_item4 = models.CharField(max_length=255)

class Team_Member(models.Model):
    Name = models.CharField(max_length=255)
    Profession = models.CharField(max_length=255)

class Appointment(models.Model):
    Description = models.TextField(max_length=500)

class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)



