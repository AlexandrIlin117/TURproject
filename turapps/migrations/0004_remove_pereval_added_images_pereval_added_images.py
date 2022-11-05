# Generated by Django 4.1.3 on 2022-11-04 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turapps', '0003_perevalimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pereval_added',
            name='images',
        ),
        migrations.AddField(
            model_name='pereval_added',
            name='images',
            field=models.ManyToManyField(through='turapps.PerevalImages', to='turapps.images'),
        ),
    ]
