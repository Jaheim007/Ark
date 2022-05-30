from django.contrib import admin
from .models import Site_Info, Info, Testimony, Choose, About, Banner

@admin.register(Site_Info)
class Site(admin.ModelAdmin):
    list_display = ('section_about_title','section_service_title','section_choose_title',
        'section_project_title', 'section_appoint_title', 'section_members_title', 
        'section_testimony_title', 'phone_number', 'location', 
        'site_link' , 'site_name', 'logo')

@admin.register(Info)
class Info(admin.ModelAdmin):
    list_display = ('image',  'title' , 'description' )

@admin.register(Testimony)
class Testimony(admin.ModelAdmin):
    list_display = ('images', 'client_name', 'profession' , 'description' )

@admin.register(Choose)
class Choose(admin.ModelAdmin):
    list_display = ('image', 'description')

@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('image', 'description', 'experience')

@admin.register(Banner)
class Banner(admin.ModelAdmin):
    list_display = ('images', 'description')


# Register your models here.
