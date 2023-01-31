from django.shortcuts import render, redirect
from .models import About, WhyUs, Category, Dish, Event, Reservation,\
    GalleryPhoto, Chef, Testimonial, Hero, Contact
from datetime import date
from .forms import ReservationForm, MessageForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name="manager").exists()


def main(request):

    if request.method == "POST":
        form_reserve = ReservationForm(request.POST)
        form_message = MessageForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect("/")
        if form_message.is_valid():
            form_message.save()
            return redirect("/")

    heroes = Hero.objects.filter(is_visible=True).order_by("position")
    abouts = About.objects.filter(is_visible=True)
    why_uses = WhyUs.objects.all()
    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    events = Event.objects.filter(is_visible=True, event_date_time__gte=date.today())
    gallery_photos = GalleryPhoto.objects.filter(is_visible=True).order_by("?")[:8]
    chefs = Chef.objects.filter(is_visible=True).order_by("position")
    testimonials = Testimonial.objects.filter(is_visible=True)
    form_reserve = ReservationForm()
    contacts = Contact.objects.all()
    form_message = MessageForm()

    return render(request, "main_page.html", context={
        "abouts": abouts,
        "why_uses": why_uses,
        "categories": categories,
        "dishes": dishes,
        "special_dishes": special_dishes,
        "events": events,
        "gallery_photos": gallery_photos,
        "chefs": chefs,
        "testimonials": testimonials,
        "heroes": heroes,
        "form_reserve": form_reserve,
        "contacts": contacts,
        "form_message": form_message,
    })


@login_required(login_url="/login/")
@user_passes_test(is_manager)
def update_reservation(request, pk):
    Reservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect("main_page:list_reservation")


@login_required(login_url="/login/")
@user_passes_test(is_manager)
def list_reservation(request):
    messages = Reservation.objects.filter(is_processed=False)
    return render(request, "reservations.html", context={"reservations": messages})



