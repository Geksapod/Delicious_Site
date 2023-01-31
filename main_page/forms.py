from django import forms
from .models import Reservation, Message


class ReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "type": "text",
        "name": "name",
        "class": "form-control",
        "id": "name",
        "placeholder": "Your Name",
        "data-rule": "minlen:4",
        "data-msg": "Please enter at least 4 chars"
    }))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "type": "email",
        "class": "form-control",
        "name": "email",
        "id": "email",
        "placeholder": "Your Email",
        "data-rule": "email",
        "data-msg": "Please enter a valid email"
    }))
    phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "type": "text",
        "class": "form-control",
        "name": "phone",
        "id": "phone",
        "placeholder": "Your Phone",
        "data-rule": "minlen:4",
        "data-msg": "Please enter at least 4 chars"
    }))
    date = forms.DateField(widget=forms.DateInput(attrs={
        "type": "date",
        "name": "date",
        "class": "form-control",
        "id": "date",
        "placeholder": "Date",
        "data-rule": "minlen:4",
        "data-msg": "Please enter at least 4 chars"
    }))
    time = forms.TimeField(widget=forms.TimeInput(attrs={
        "type": "time",
        "class": "form-control",
        "name": "time",
        "id": "time",
        "placeholder": "Time",
        "data-rule": "minlen:4",
        "data-msg": "Please enter at least 4 chars"
    }))
    number_of_people = forms.IntegerField(widget=forms.NumberInput(attrs={
        "type": "number",
        "class": "form-control",
        "name": "people",
        "id": "people",
        "placeholder": "# of people",
        "min": "1",
        "data-rule": "minlen:1",
        "data-msg": "Please enter at least 1 chars"
    }))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        "class": "form-control",
        "name": "message",
        "rows": "5",
        "placeholder": "Message"
    }))

    class Meta:
        model = Reservation
        fields = ["name",
                  "email",
                  "phone",
                  "date",
                  "time",
                  "number_of_people",
                  "message"]


class MessageForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "type": "text",
        "name": "name",
        "class": "form-control",
        "id": "name",
        "placeholder": "Your Name",
        "data-rule": "minlen:4",
        "data-msg": "Please enter at least 4 chars"
    }))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "type": "email",
        "class": "form-control",
        "name": "email",
        "id": "email",
        "placeholder": "Your Email",
        "data-rule": "email",
        "data-msg": "Please enter a valid email"
    }))
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "type": "text",
        "name": "subject",
        "class": "form-control",
        "id": "subject",
        "placeholder": "Subject",
        "data-rule": "minlen:4",
        "data-msg": "Please enter at least 4 chars",
    }))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        "class": "form-control",
        "name": "message",
        "rows": "5",
        "placeholder": "Message"
    }))

    class Meta:
        model = Message
        fields = ["name",
                  "email",
                  "subject",
                  "message"]





