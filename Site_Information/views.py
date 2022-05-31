from django.shortcuts import render
from .models import Banner, Info, About, Testimony, Choose
from Services_Information.models import Service, Project, Team_Member


def index(request):
    banner = Banner.objects.all()
    info = Info.objects.all()
    about  = About.objects.filter().first()
    service = Service.objects.all()
    project = Project.objects.all()
    team = Team_Member.objects.all()
    test = Testimony.objects.all()
    choose = Choose.objects.all()
    num = 0
    return render(request, 'pages/index.html', locals())

def error(request):
    return render(request, 'pages/404.html')

def about(request):
    return render(request, 'pages/about.html')

def appoint(request):
    return render(request, 'pages/appointment.html')

def contact(request):
    return render(request, 'pages/contact.html')

def feature(request):
    return render(request, 'pages/feature.html')

def project(request):
    return render(request, 'pages/project.html')

def service(request):
    return render(request, 'pages/service.html')

def team(request):
    return render(request, 'pages/team.html')

def testimonial(request):
    return render(request, 'pages/testimonial.html')



# Create your views here.
