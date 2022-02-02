from django.shortcuts import render, get_object_or_404
from .models import Laptop
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def laptops(request):
    laptops = Laptop.objects.order_by('-created_date')
    paginator = Paginator(laptops, 2)
    page = request.GET.get('page')
    paged_laptops = paginator.get_page(page)
    brand_search = Laptop.objects.values_list('brand', flat=True).distinct()
    model_search = Laptop.objects.values_list('model', flat=True).distinct()
    ram_search = Laptop.objects.values_list('ram', flat=True).distinct()
    processor_search = Laptop.objects.values_list('processor', flat=True).distinct()
    display_search = Laptop.objects.values_list('display', flat=True).distinct()

    data = {
        'laptops' : paged_laptops,
        'brand_search':brand_search,
        'model_search':model_search,
        'ram_search':ram_search,
        'processor_search':processor_search,
        'display_search':display_search,

    }
    return render(request, 'laptops/laptops.html', data)

def laptop_detail(request, id):
    single_laptop = get_object_or_404(Laptop, pk=id)
    data = {
        'single_laptop' : single_laptop

    }
    return render(request, 'laptops/laptop_detail.html', data)

def search(request):
    laptops = Laptop.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            laptops = laptops.filter(description__icontains=keyword)

    if 'brand' in request.GET:
        brand = request.GET['brand']
        if brand:
            laptops = laptops.filter(brand__iexact=brand)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            laptops = laptops.filter(model__iexact=model)

    if 'ram' in request.GET:
        ram = request.GET['ram']
        if ram:
            laptops = laptops.filter(ram__iexact=ram)

    if 'display' in request.GET:
        display = request.GET['display']
        if display:
            laptops = laptops.filter(display__iexact=display)

    if 'processor' in request.GET:
        processor = request.GET['processor']
        if processor:
            laptops = laptops.filter(processor__iexact=processor)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            laptops = laptops.filter(price__gte=min_price, price__lte=max_price)

    brand_search = Laptop.objects.values_list('brand', flat=True).distinct()
    model_search = Laptop.objects.values_list('model', flat=True).distinct()
    ram_search = Laptop.objects.values_list('ram', flat=True).distinct()
    processor_search = Laptop.objects.values_list('processor', flat=True).distinct()
    display_search = Laptop.objects.values_list('display', flat=True).distinct()

    data = {
        'laptops':laptops,
        'brand_search':brand_search,
        'model_search':model_search,
        'ram_search':ram_search,
        'processor_search':processor_search,
        'display_search':display_search,

    }
    return render(request, 'laptops/search.html', data)
