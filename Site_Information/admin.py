from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Site_Info, Info, Testimony, Choose, About, Banner

@admin.register(Site_Info)
class Site(admin.ModelAdmin):
    list_display = ('views', 'section_about_title','section_service_title','section_choose_title',
        'section_project_title', 'section_appoint_title', 'section_members_title', 
        'section_testimony_title', 'phone_number', 'location', 
        'site_email', 'site_address' , 'site_name', )
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.logo.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 

@admin.register(Info)
class Info(admin.ModelAdmin):
    list_display = ('views',  'title' , 'description' )
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.image.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 

@admin.register(Testimony)
class Testimony(admin.ModelAdmin):
    list_display = ('views', 'client_name', 'profession' , 'description' )
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.images.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images'

@admin.register(Choose)
class Choose(admin.ModelAdmin):
    list_display = ('description',)
    

@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('views','view', 'description', 'experience')
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.image1.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 
    
    def view(self, obj):     
        return mark_safe(f'<img src="{obj.image2.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 

@admin.register(Banner)
class Banner(admin.ModelAdmin):
    list_display = ('views', 'title', 'description')
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.images.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 


# Register your models here.
