# Generated by Django 3.0.7 on 2022-01-31 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0002_laptop_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='ram',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
