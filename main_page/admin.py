from django.contrib import admin
from .models import About, WhyUs, Category, Dish, Event, \
    Reservation, GalleryPhoto, Chef, Testimonial, Hero, Contact, Message

# Register your models here.


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    model = Hero
    list_display = ["title",
                    "position",
                    "is_visible",
                    "text",
                    ]
    list_filter = ["position",
                   "is_visible",
                   ]
    list_editable = ["is_visible",
                     "text",
                     ]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    model = About
    list_display = ["title",
                    "position",
                    "is_visible",
                    ]
    list_editable = ["is_visible",
                     ]


@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):
    model = WhyUs
    list_display = ["title",
                    "position",
                    "text",
                    ]
    list_filter = ["position"]
    list_editable = ["position",
                     "text",
                     ]


class DishAdmin(admin.TabularInline):
    model = Dish
    raw_id_fields = ["category"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "position", "is_visible"]
    list_editable = ["position", "is_visible"]
    inlines = [DishAdmin]


@admin.register(Dish)
class DishAllAdmin(admin.ModelAdmin):
    model = Dish
    list_display = ["title",
                    "position",
                    "is_visible",
                    "ingredients",
                    "description",
                    "price",
                    "photo",
                    "category",
                    "is_special",
                    ]
    list_filter = ["category",
                   "is_visible",
                   "is_special",
                   ]
    list_editable = ["position",
                     "is_visible",
                     "price",
                     "is_special",
                     ]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ["title",
                    "is_visible",
                    "price",
                    "photo",
                    "event_date_time",
                    ]
    list_filter = ["is_visible",
                   "event_date_time",
                   ]
    list_editable = ["is_visible",
                     "price",
                     "event_date_time",
                     ]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ["name",
                    "phone",
                    "date_incoming",
                    "is_processed",
                    "date_processing",
                    ]
    list_filter = ["is_processed",
                   ]
    list_editable = ["is_processed",
                     ]


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    model = GalleryPhoto
    list_display = ["photo_preview",
                    "is_visible",
                    ]
    list_filter = ["is_visible",
                   ]
    list_editable = ["is_visible",
                     ]


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    model = Chef
    list_display = ["surname",
                    "name",
                    "specialty",
                    "position",
                    "is_visible",
                    ]
    list_filter = ["position",
                   "is_visible",
                   ]
    list_editable = ["is_visible",
                     "position",
                     "specialty",
                     ]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    model = Testimonial
    list_display = ["full_name",
                    "occupation",
                    "comment",
                    "is_visible",
                    ]
    list_filter = ["is_visible",
                   ]
    list_editable = ["is_visible",
                     "occupation",
                     "comment",
                     ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ["name",
                    "email",
                    "subject",
                    "date_incoming",
                    "viewed",
                    ]
    list_filter = ["viewed",
                   ]
    list_editable = ["viewed",
                     ]
