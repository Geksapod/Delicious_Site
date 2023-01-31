# Generated by Django 4.1.5 on 2023-02-09 10:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0009_hero_background_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('email', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Error email', regex='(\\w+[-_.]?\\w+)+@(\\w+.)+[A-Za-z]+')])),
                ('phone', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Error phone number', regex='^\\+?3?8?0\\d{2}[- ]?(\\d[ -]?){7}?')])),
                ('booking_time', models.DateTimeField()),
                ('number_of_people', models.PositiveIntegerField()),
                ('message', models.TextField(blank=True, max_length=1000)),
                ('date_incoming', models.DateTimeField(auto_now_add=True)),
                ('date_processing', models.DateTimeField(auto_now=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date_incoming',),
            },
        ),
    ]