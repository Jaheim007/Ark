from django.db import models

class Site_Info(models.Model):
    section_about_title = models.CharField(max_length=255)
    section_service_title = models.CharField(max_length=255)
    section_choose_title = models.CharField(max_length=255)
    section_project_title = models.CharField(max_length=255)
    section_appoint_title = models.CharField(max_length=255)
    section_members_title = models.CharField(max_length=255)
    section_testimony_title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    location = models.URLField(max_length=255)
    site_email = models.EmailField(max_length=254)
    site_address  = models.CharField(max_length=255)
    site_name = models.CharField(max_length=255)
    logo = models.FileField()

    def __str__(self):
        return self.section_about_title

class Banner(models.Model):
    images = models.FileField()
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Testimony(models.Model):
    images = models.FileField()
    client_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.client_name

class Info(models.Model):
    image = models.FileField()
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class About(models.Model):
    image1 = models.FileField()
    image2 = models.FileField()
    description = models.TextField(max_length=500)
    experience = models.IntegerField()

    def __str__(self):
        return self.description

class Choose(models.Model):
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.description




    

