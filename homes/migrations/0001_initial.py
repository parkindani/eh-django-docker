# Generated by Django 3.2 on 2021-04-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_name', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('geo_lat', models.CharField(max_length=500)),
                ('geo_lng', models.CharField(max_length=500)),
                ('max_capacity', models.IntegerField(default=0)),
                ('current_person', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('update_date', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
    ]
