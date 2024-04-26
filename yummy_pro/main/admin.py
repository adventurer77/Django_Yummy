from django.contrib import admin
from .models import DishCategory,Dish,Gallery,Staff,ChefSocialMediaLink,Events,Contacts
from django.utils.safestring import mark_safe


# Register your models here.

# admin.site.register(DishCategory)
@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name","is_visible", "sort",'slug')
    list_editable = ("name","is_visible", "sort",'slug')
    list_filter = ("is_visible",)
    search_fields = ("name",)
    prepopulated_fields = {"slug" : ("name",)}

# admin.site.register(Dish)
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("photo_src_tag","name","ingredients", "price", "is_visible", "sort", "category")

    list_editable = ("ingredients", "price", "is_visible","sort")
    list_filter = ("category", "is_visible")
    search_fields = ("name",)

    def photo_src_tag(self,obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")
    
    photo_src_tag.short_description = "Dish photo"


# admin.site.register(Events)
@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ("photo_src_tag","title", "price","description", "is_visible", "sort")

    list_editable = ("title", "price","description", "is_visible","sort")
    list_filter = ("is_visible",)
    search_fields = ("title",)

    def photo_src_tag(self,obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")
    
    photo_src_tag.short_description = "Event photo"


# admin.site.register(Staff)
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("photo_src_tag","name","position","description", "is_visible",'sort')

    list_editable = ("name","position","description", "is_visible",'sort')
    list_filter = ("is_visible",)
    search_fields = ("name","position")

    def photo_src_tag(self,obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")
    
    photo_src_tag.short_description = "Staff photo"


@admin.register(ChefSocialMediaLink)
class ChefSocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('chef', 'platform', 'url')
    list_editable = ('platform', 'url')
    search_fields = ('platform', 'url')
    list_filter = ('chef',)


# admin.site.register(Gallery) 
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("photo_src_tag","name","is_visible")

    list_editable = ("name","is_visible")
    list_filter = ("is_visible",)
    search_fields = ("name",)

    def photo_src_tag(self,obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")
    
    photo_src_tag.short_description = "Gallery photo"


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):

    list_display = ("address","email","phone_number","opening_hours")

    list_editable = ("email","phone_number","opening_hours")
    search_fields = ("address",)