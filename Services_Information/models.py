from email.mime import image
from turtle import title
from xml.parsers.expat import model
from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.FileField()
    logo = models.FileField()

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    list_item = models.CharField(max_length=255)
    image = models.FileField()

class Team_Member(models.Model):
    Name = models.CharField(max_length=255)
    Profession = models.CharField(max_length=255)
    image = models.FileField()
    
    

class Appointment(models.Model):
    Description = models.TextField(max_length=500)

class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)



