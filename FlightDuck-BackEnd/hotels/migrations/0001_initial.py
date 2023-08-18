# Generated by Django 2.2 on 2021-11-13 21:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelBedsLastUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HotelBookingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now=True)),
                ('booking_reference', models.CharField(max_length=50)),
                ('booking_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='HotelCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.CharField(max_length=20, unique=True)),
                ('accomodation_type', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HotelCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=20, unique=True)),
                ('iso_code', models.CharField(max_length=20)),
                ('country_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HotelDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=900)),
                ('city', models.CharField(default='', max_length=200)),
                ('destination_code', models.CharField(default='', max_length=10)),
                ('category_code', models.CharField(default='', max_length=10)),
                ('health_safety_code', models.CharField(default='', max_length=10)),
                ('latitude', models.DecimalField(decimal_places=3, default=0, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=3, default=0, max_digits=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.HotelCountry')),
            ],
        ),
        migrations.CreateModel(
            name='HotelFacilityDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_code', models.IntegerField()),
                ('facility_group_code', models.IntegerField()),
                ('facility_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SearchHotelCountryWiseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_iso_code', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='SearchHotelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=10)),
                ('checkInDate', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Length has to be 10', regex='^.{10}$')])),
                ('checkOutDate', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Length has to be 10', regex='^.{10}$')])),
                ('rooms', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('adults', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('children', models.IntegerField(blank=True, default=0)),
                ('user_id', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minPax', models.IntegerField()),
                ('maxPax', models.IntegerField()),
                ('maxAdults', models.IntegerField()),
                ('maxChildren', models.IntegerField()),
                ('minAdults', models.IntegerField()),
                ('hotel', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='hotels.HotelDetail')),
            ],
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=1000)),
                ('hotel', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='hotels.HotelDetail')),
            ],
        ),
        migrations.CreateModel(
            name='HotelFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=300)),
                ('facility_chargeable', models.BooleanField(blank=True, default=False)),
                ('facility_available', models.BooleanField(blank=True, default=False)),
                ('facility_time_from', models.TimeField(blank=True, null=True)),
                ('facility_time_to', models.TimeField(blank=True, null=True)),
                ('hotel', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='hotels.HotelDetail')),
            ],
        ),
        migrations.CreateModel(
            name='HotelDestinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('iso_code', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.HotelCountry')),
            ],
        ),
        migrations.CreateModel(
            name='HotelCountryState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_code', models.CharField(max_length=20)),
                ('state_name', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.HotelCountry')),
            ],
        ),
    ]