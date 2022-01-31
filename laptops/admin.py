from django.contrib import admin
from .models import Laptop
from django.utils.html import format_html
# Register your models here.

class LaptopAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;"/>'.format(object.laptop_image.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'laptop_title', 'model', 'ram', 'processor', 'price', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'laptop_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'laptop_title', 'model',)
    list_filter = ('model', 'price',)

admin.site.register(Laptop, LaptopAdmin)
