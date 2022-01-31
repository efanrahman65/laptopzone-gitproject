from django.shortcuts import render
from .models import Team
from laptops.models import Laptop
# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_laptops = Laptop.objects.order_by('-created_date').filter(is_featured=True)
    all_laptops = Laptop.objects.order_by('-created_date')
    data = {
    'teams':teams,
    'featured_laptops':featured_laptops,
    'all_laptops':all_laptops
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
    'teams':teams
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
