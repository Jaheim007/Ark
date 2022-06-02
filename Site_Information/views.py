from threading import local
from django.shortcuts import render
from .models import Banner, Info, About, Testimony, Choose, Site_Info
from Services_Information.models import Service, Project, Team_Member


def index(request):
    site = Site_Info.objects.filter().first()
    banner = Banner.objects.all()
    info = Info.objects.all()
    about  = About.objects.filter().first()
    about_full = About.objects.all()
    service = Service.objects.all()
    project = Project.objects.all()
    team = Team_Member.objects.all()
    test = Testimony.objects.all()
    choose = Choose.objects.all()
    return render(request, 'pages/index.html', locals())

def error(request):
    return render(request, 'pages/404.html', locals())

def about(request):
    site = Site_Info.objects.filter().first()
    about1 = About.objects.filter().first()
    about_full = About.objects.all()
    choose = Choose.objects.all()
    team = Team_Member.objects.all()
    info = Info.objects.all()
    return render(request, 'pages/about.html' , locals())

def appoint(request):
    site = Site_Info.objects.filter().first()
    return render(request, 'pages/appointment.html', locals())

def contact(request):
    site = Site_Info.objects.filter().first()
    return render(request, 'pages/contact.html', locals())

def feature(request):
    choose = Choose.objects.all()
    info = Info.objects.all()
    about_full = About.objects.all()
    site = Site_Info.objects.filter().first()
    return render(request, 'pages/feature.html', locals())

def project(request):
    project = Project.objects.all()
    info = Info.objects.all()
    site = Site_Info.objects.filter().first()
    return render(request, 'pages/project.html',locals() )

def service(request):
    info = Info.objects.all()
    service = Service.objects.all()
    test = Testimony.objects.all()
    site = Site_Info.objects.filter().first()
    return render(request, 'pages/service.html', locals())

def team(request):
    team = Team_Member.objects.all()
   
    
    site = Site_Info.objects.filter().first()
    return render(request, 'pages/team.html', locals())

def testimonial(request):
    test = Testimony.objects.all()
    site = Site_Info.objects.filter().first()
    return render(request, 'pages/testimonial.html', locals())



# Create your views here.
