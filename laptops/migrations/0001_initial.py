# Generated by Django 3.0.7 on 2022-01-30 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laptop_title', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], verbose_name='year')),
                ('model', models.CharField(max_length=255)),
                ('processor', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('storage', models.CharField(max_length=255)),
                ('display', models.CharField(max_length=255)),
                ('laptop_image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('laptop_image_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('laptop_image_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('laptop_image_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('laptop_image_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
