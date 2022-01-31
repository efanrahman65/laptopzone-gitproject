from django.shortcuts import render

# Create your views here.
def laptops(request):
    return render(request, 'laptops/laptops.html')
