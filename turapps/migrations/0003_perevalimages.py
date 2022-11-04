# Generated by Django 4.1.3 on 2022-11-04 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turapps', '0002_alter_pereval_added_coords_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turapps.images')),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turapps.pereval_added')),
            ],
        ),
    ]