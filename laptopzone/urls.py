
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('laptops/', include('laptops.urls')),
    path('accounts/', include('accounts.urls')),
    path('socialaccounts/', include('allauth.urls')),
    path('contacts/', include('contacts.urls')),
    path('shop/', include('App_Order.urls')),
    path('payment/', include('App_Payment.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
