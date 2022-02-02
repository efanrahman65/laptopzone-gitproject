from django.shortcuts import render
from .models import Team
from laptops.models import Laptop
# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_laptops = Laptop.objects.order_by('-created_date').filter(is_featured=True)
    all_laptops = Laptop.objects.order_by('-created_date')

    #search_fields = Laptop.objects.values('model', 'ram', 'brand', 'color','processor','display')
    brand_search = Laptop.objects.values_list('brand', flat=True).distinct()
    model_search = Laptop.objects.values_list('model', flat=True).distinct()
    ram_search = Laptop.objects.values_list('ram', flat=True).distinct()
    processor_search = Laptop.objects.values_list('processor', flat=True).distinct()
    display_search = Laptop.objects.values_list('display', flat=True).distinct()
    data = {
    'teams':teams,
    'featured_laptops':featured_laptops,
    'all_laptops':all_laptops,
    'brand_search':brand_search,
    'model_search':model_search,
    'ram_search':ram_search,
    'processor_search':processor_search,
    'display_search':display_search,
    #'search_fields':search_fields
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
