from django.shortcuts import render
from django.http import HttpResponse
from .models import DishCategory,Dish,Gallery,Staff,ChefSocialMediaLink,Events,Contacts

# Create your views here.

def index(request):
    # categories = DishCategory.objects.all()
    # categories = DishCategory.objects.get(id=1)
    # categories = DishCategory.objects.filter(is_visible=True)
    # for item in categories:
    #     for dish in item.dish_set.filter(is_visible=True): # dish_set - name of the table associated with this one is written in lowercase letters
    #         print(dish.name)
    #     print(item.name)
    
    # categories = DishCategory.objects.filter(is_visible=True)
    # for item in categories:
    #     for dish in Dish.objects.filter(category=item, is_visible=True): # V2
    #         print(dish.name)
    #     print(item.name)


    # categories = DishCategory.objects.filter(is_visible=True) # V3
    # for item in categories:
    #     for dish in item:
    #         print(dish.name)
    #     print(item.name)

    categories = DishCategory.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    staff = Staff.objects.filter(is_visible=True)
    events = Events.objects.filter(is_visible=True)
    contacts = Contacts.objects.first()


    contact_details = []
    if contacts: 
        contact_details = [
                    { "title": "Our Address", "content": contacts.address},
                    { "title": "Email Us", "content": contacts.email},
                    {  "title": "Call Us", "content": contacts.phone_number},
                    {  "title": "Opening Hours", "content": contacts.opening_hours},
                ]

    context = {
        'title_menu': 'Check Our <span>Yummy Menu</span>',
        'title_callery': "Check <span>Our Gallery</span>",
        'title_staff': "Our <span>Proffesional</span> Chefs",
        'title_events': "Share <span>Your Moments</span> In Our Restaurant",
        'title_contacts': "Need Help? <span>Contact Us</span>",

        "categories" : categories,
        "gallery" : gallery,
        "staff" : staff,
        "events" : events,
        "contacts": contacts,
        "contact_details" : contact_details,
    }
    
    return render(request, "main.html", context=context)

def manager(request):
    ...

#    return render(request, "index.html")

    # return HttpResponse("\n".join(map(str,categories)))