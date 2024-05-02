from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField

# Create your models here.

class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()


    def __str__(self) -> str:
        return self.name

    def __iter__(self):
        for item in self.dishes.filter(is_visible=True): # V3
            yield item


    class Meta:
        verbose_name = "Category of dish"
        verbose_name_plural = "Categories of dishes"
        ordering = ["sort"]
        # ordering = ["-sort"]

class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name="dishes")
    sort = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to="dishes/", blank=True, null=True)


    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"
        ordering = ["sort"]

    

class Events(models.Model):
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=400, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to="events/", blank=True, null=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["sort"]


    def __str__(self):
        return self.title
    
    # def __str__(self) -> str:
    #     description_snippet = self.description[:20] + "..." if len(self.description) > 20 else self.description
    #     return f"{self.name} (Price: {self.price:.2f}, Description: {description_snippet})"


class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(max_length=400, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    image = models.ImageField(upload_to="staff/", blank=True, null=True)
    sort = models.PositiveSmallIntegerField()
    

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Staff"
        ordering = ['sort']
        
    def __iter__(self):
        for item in self.staff.all(): # V3
            yield item

    def __str__(self) -> str:
        return self.name
    



class ChefSocialMediaLink(models.Model):
    chef = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="staff") 
    platform = models.CharField(max_length=20)  
    url = models.URLField(blank=True, null=True)  
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.chef.name} - {self.platform}"
    
    class Meta:
        verbose_name = "Platform"
        verbose_name_plural = "Platforms"
        ordering = ['sort']


class Gallery(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Gallery"
        ordering = ['name']


class Contacts(models.Model):

    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, help_text='Enter phone number')
    opening_hours = RichTextField(blank=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['address']

    def __str__(self):
        return self.address 
    


class Reservation(models.Model):
    phone_regex = RegexValidator(regex=r"^\+?(380)?\d{9,15}$",
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, validators=[phone_regex])
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    count = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.date} {self.time}'

    
    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservation"
        ordering = ["-date_created"]

