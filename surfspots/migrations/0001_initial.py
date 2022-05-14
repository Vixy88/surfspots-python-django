# Generated by Django 4.0.4 on 2022-05-14 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surfspot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('country', models.CharField(default=None, max_length=100)),
                ('address', models.CharField(default=None, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('postcode', models.CharField(default=None, max_length=100)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, default='0', max_digits=9)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, default='0', max_digits=9)),
                ('image', models.CharField(default=None, max_length=250)),
                ('magic_seaweed_link', models.CharField(default=None, max_length=250)),
                ('google_directions_link', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('restaurants_nearby', models.ManyToManyField(blank=True, related_name='surfspots_nearby', to='restaurants.restaurant')),
            ],
        ),
    ]
