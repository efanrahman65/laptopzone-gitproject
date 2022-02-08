from django.shortcuts import render, redirect
from .models import Team
from laptops.models import Laptop
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
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
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Laptopzone website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'efanrahman32824@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'pages/contact.html')
