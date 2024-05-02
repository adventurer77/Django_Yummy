from typing import Any
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import DishCategory,Dish,Gallery,Staff,ChefSocialMediaLink,Events,Contacts
from .forms import ReservationForm
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required,user_passes_test

def is_manager(user):
    return user.groups.filter(name="manager").exists()

# Create your views here.

class IndexView(TemplateView):

    template_name = "main.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        gallery = Gallery.objects.filter(is_visible=True)
        staff = Staff.objects.filter(is_visible=True)
        events = Events.objects.filter(is_visible=True)
        contacts = Contacts.objects.first()
        form = ReservationForm()

        contact_details = []
        if contacts: 
            contact_details = [
                        { "title": "Our Address", "content": contacts.address},
                        { "title": "Email Us", "content": contacts.email},
                        {  "title": "Call Us", "content": contacts.phone_number},
                        {  "title": "Opening Hours", "content": contacts.opening_hours},
                    ]

    
        context['title_menu'] = 'Check Our <span>Yummy Menu</span>'
        context['title_callery'] =  "Check <span>Our Gallery</span>"
        context['title_staff'] = "Our <span>Proffesional</span> Chefs"
        context['title_events'] = "Share <span>Your Moments</span> In Our Restaurant"
        context['title_contacts'] = "Need Help? <span>Contact Us</span>"
        context['title_reservation'] = "Book <span>Your Stay</span> With Us"
        context['button_reservation'] = "Book A Table"



        context["categories"] = categories
        context["gallery"] = gallery
        context["staff"] = staff
        context["events"] = events
        context["contacts"] = contacts
        context["contact_details"] = contact_details
        context["form"] = form
    
        return context
    
    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your reservation has been accepted!")
            return redirect('main:index')
        else:
            
            messages.error(request, "There were errors in your reservation form. Please correct and try again.")
            
            return redirect( 'main:index')
            
            
        

@login_required(login_url="/login/")
@user_passes_test(is_manager)       
def manager(request):
    return HttpResponse("Manager page")

# def index(request):
#     # categories = DishCategory.objects.all()
#     # categories = DishCategory.objects.get(id=1)
#     # categories = DishCategory.objects.filter(is_visible=True)
#     # for item in categories:
#     #     for dish in item.dish_set.filter(is_visible=True): # dish_set - name of the table associated with this one is written in lowercase letters
#     #         print(dish.name)
#     #     print(item.name)
    
#     # categories = DishCategory.objects.filter(is_visible=True)
#     # for item in categories:
#     #     for dish in Dish.objects.filter(category=item, is_visible=True): # V2
#     #         print(dish.name)
#     #     print(item.name)


#     # categories = DishCategory.objects.filter(is_visible=True) # V3
#     # for item in categories:
#     #     for dish in item:
#     #         print(dish.name)
#     #     print(item.name)

#     categories = DishCategory.objects.filter(is_visible=True)
#     gallery = Gallery.objects.filter(is_visible=True)
#     staff = Staff.objects.filter(is_visible=True)
#     events = Events.objects.filter(is_visible=True)
#     contacts = Contacts.objects.first()


#     contact_details = []
#     if contacts: 
#         contact_details = [
#                     { "title": "Our Address", "content": contacts.address},
#                     { "title": "Email Us", "content": contacts.email},
#                     {  "title": "Call Us", "content": contacts.phone_number},
#                     {  "title": "Opening Hours", "content": contacts.opening_hours},
#                 ]

#     context = {
#         'title_menu': 'Check Our <span>Yummy Menu</span>',
#         'title_callery': "Check <span>Our Gallery</span>",
#         'title_staff': "Our <span>Proffesional</span> Chefs",
#         'title_events': "Share <span>Your Moments</span> In Our Restaurant",
#         'title_contacts': "Need Help? <span>Contact Us</span>",

#         "categories" : categories,
#         "gallery" : gallery,
#         "staff" : staff,
#         "events" : events,
#         "contacts": contacts,
#         "contact_details" : contact_details,
#     }
    
#     return render(request, "main.html", context=context)

# def manager(request):
#     ...

#    return render(request, "index.html")

    # return HttpResponse("\n".join(map(str,categories)))