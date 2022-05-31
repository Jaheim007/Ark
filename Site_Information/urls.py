from django.urls import path 
from .views import index, testimonial, service, project , error, contact, about, feature, appoint, team

urlpatterns = [
    path('', index , name='index'),
    path('team', team , name='team'),
    path('testimonial', testimonial , name='testimonial'),
    path('error', error , name='error'),
    path('contact', contact , name='contact'),
    path('appoint', appoint , name='appoint'),
    path('service', service , name='service'),
    path('error', error , name='error'),
    path('about', about , name='about'),
    path('feature', feature , name='feature'),
    path('project', project , name='project'),
    path('project', project , name='project'),
    
]
