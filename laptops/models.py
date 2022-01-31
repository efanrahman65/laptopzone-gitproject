from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Laptop(models.Model):

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))


    laptop_title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    year = models.IntegerField(('year'), choices=year_choice)
    model = models.CharField(max_length=255)
    #ram = models.CharField(max_length=100)
    ram = models.CharField(max_length=100, null=True)
    processor = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    price = models.IntegerField()
    storage = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    laptop_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    laptop_image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    laptop_image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    laptop_image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    laptop_image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    description = RichTextField(null=True)

    def __str__(self):
        return self.laptop_title
