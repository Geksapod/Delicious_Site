# Generated by Django 4.1.5 on 2023-02-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0011_remove_reservation_booking_time_reservation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]