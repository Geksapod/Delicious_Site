# Generated by Django 4.1.5 on 2023-02-15 16:37

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0012_alter_reservation_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutparagraph',
            name='about',
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ('-date_processing',)},
        ),
        migrations.RemoveField(
            model_name='about',
            name='header',
        ),
        migrations.RemoveField(
            model_name='about',
            name='header_strong',
        ),
        migrations.AddField(
            model_name='about',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Error phone number', regex='^\\+?3?8?[ (]?0\\d{2}[)]?[- ]?\\d{3}[ -]?\\d{2}[ -]?\\d{2}$')]),
        ),
        migrations.DeleteModel(
            name='AboutList',
        ),
        migrations.DeleteModel(
            name='AboutParagraph',
        ),
    ]
