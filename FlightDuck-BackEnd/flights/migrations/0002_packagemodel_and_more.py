# Generated by Django 4.2.3 on 2023-08-01 17:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=10)),
                ('destination', models.CharField(max_length=10)),
                ('outbound_date', models.CharField(max_length=10)),
                ('adults', models.IntegerField(default=0)),
                ('children', models.IntegerField(default=0)),
                ('country', models.CharField(max_length=10)),
                ('currency_format', models.CharField(max_length=10)),
                ('locale', models.CharField(max_length=10)),
                ('destination_code', models.CharField(blank=True, default='', max_length=10)),
                ('trip_days', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30)])),
                ('number_of_extended_months', models.IntegerField(default=0)),
                ('user_id', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='flightshotelpackagemodel',
            name='inbounddate',
            field=models.CharField(max_length=20),
        ),
    ]