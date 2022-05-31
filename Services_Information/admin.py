from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Service, Project, Team_Member, Appointment, Newsletter

@admin.register(Service)
class Service(admin.ModelAdmin):   
    list_display = ('views','view', 'title', 'description' )
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.image.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images'
    
    def view(self, obj):     
        return mark_safe(f'<img src="{obj.logo.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images'

@admin.register(Project)
class Project(admin.ModelAdmin):   
    list_display = ('views', 'title', 'description', 'list_item' )
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.image.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images'

@admin.register(Team_Member)
class Team(admin.ModelAdmin):   
    list_display = ('views','Name', 'Profession')
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.image.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images'

@admin.register(Appointment)
class Appoint(admin.ModelAdmin):   
    list_display = ('Description',)

@admin.register(Newsletter)
class News(admin.ModelAdmin):   
    list_display = ('title', 'description', 'Email' )




# Register your models here.
