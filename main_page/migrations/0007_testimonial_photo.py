# Generated by Django 4.1.5 on 2023-02-08 15:26

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='photo',
            field=models.ImageField(blank=True, upload_to=main_page.models.get_file_name),
        ),
    ]
