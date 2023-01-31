from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.validators import RegexValidator
from pattern.en import pluralize
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
import uuid
import os
import time


def get_file_name(cls, file_name):

    extension = file_name.strip().split(".")[-1]
    file_name = f"{uuid.uuid4()}.{extension}"
    return os.path.join(f"{pluralize(type(cls).__name__)}", f"{time.strftime('%Y_%m_%d', time.gmtime())}", file_name)


class Hero(models.Model):

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    text = models.TextField(max_length=500)
    background_photo = models.ImageField(upload_to=get_file_name, blank=True)


class About(models.Model):

    position = models.SmallIntegerField(unique=True, db_index=True)
    title = models.CharField(max_length=50, default="About us")
    text = RichTextField(blank=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    video = models.FileField(upload_to=get_file_name,
                             blank=True,
                             validators=[FileExtensionValidator(allowed_extensions=['MOV',
                                                                                    'avi',
                                                                                    'mp4',
                                                                                    'webm',
                                                                                    'mkv'])])

    def __str__(self):
        return f"{self.title}"


class WhyUs(models.Model):

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    text = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ("position", )


class Category(models.Model):

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ("position", )

    def __iter__(self):
        for dish in self.dishes.all():
            yield dish


class Dish(models.Model):

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="dishes")
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ("position", "price", )


class Event(models.Model):

    title = models.CharField(max_length=50, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    event_date_time = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ("event_date_time", "price", )


class Reservation(models.Model):

    email_validator = RegexValidator(regex=r"(\w+[-_.]?\w+)+@(\w+.)+[A-Za-z]+", message="Error email")
    phone_validator = RegexValidator(regex=r"^\+?3?8?[ (]?0\d{2}[)]?[- ]?\d{3}[ -]?\d{2}[ -]?\d{2}$",
                                     message="Error phone number")

    name = models.CharField(max_length=50, db_index=True)
    email = models.CharField(max_length=50, validators=[email_validator])
    phone = models.CharField(max_length=50, validators=[phone_validator])
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    number_of_people = models.PositiveIntegerField()
    message = models.TextField(max_length=1000, blank=True)

    date_incoming = models.DateTimeField(auto_now_add=True)
    date_processing = models.DateTimeField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        ordering = ("-date_processing", )


class GalleryPhoto(models.Model):

    title = models.CharField(max_length=50, unique=True, null=True, db_index=True)
    photo = models.ImageField(upload_to=get_file_name, blank=False)
    is_visible = models.BooleanField(default=True)

    def photo_preview(self):
        return mark_safe(f'<img src = "{self.photo.url}" width = "300"/>')


class Chef(models.Model):

    surname = models.CharField(max_length=50, unique=True, db_index=True)
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    position = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.surname}{self.name}"

    class Meta:
        ordering = ("position", "is_visible", )


class Testimonial(models.Model):

    full_name = models.CharField(max_length=50, unique=True, db_index=True)
    occupation = models.CharField(max_length=50)
    comment = models.CharField(max_length=300, blank=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to=get_file_name, blank=True)

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        ordering = ("is_visible", )


class Contact(models.Model):

    location = RichTextField(blank=True)
    open_hours = RichTextField(blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return "Contacts"


class Message(models.Model):

    email_validator = RegexValidator(regex=r"(\w+[-_.]?\w+)+@(\w+.)+[A-Za-z]+", message="Error email")

    name = models.CharField(max_length=50, db_index=True)
    email = models.CharField(max_length=50, validators=[email_validator])
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)

    date_incoming = models.DateTimeField(auto_now_add=True, editable=False)
    viewed = models.BooleanField(default=False)
