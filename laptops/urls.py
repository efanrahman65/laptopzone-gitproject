
from django.urls import path
from . import views

urlpatterns = [
    path('', views.laptops, name='laptops'),
    path('<int:id>', views.laptop_detail, name='laptop_detail'),
    path('search', views.search, name='search'),
]
