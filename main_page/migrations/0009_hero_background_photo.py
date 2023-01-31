# Generated by Django 4.1.5 on 2023-02-08 20:07

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_hero'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='background_photo',
            field=models.ImageField(blank=True, upload_to=main_page.models.get_file_name),
        ),
    ]