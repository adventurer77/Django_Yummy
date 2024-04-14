from django.db import models

# Create your models here.
class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()


    def __str__(self) -> str:
        return self.name
    

class Events(models.Model):
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=400, blank=False)
    is_visible = models.BooleanField(default=True)
    # image = models.ImageField(upload_to=)

    class Meta:

        ordering = ("price",)


    def __str__(self):
        return self.title
    
    # def __str__(self) -> str:
    #     description_snippet = self.description[:20] + "..." if len(self.description) > 20 else self.description
    #     return f"{self.name} (Price: {self.price:.2f}, Description: {description_snippet})"


class Personnel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=8)
    employee_status = models.BooleanField(default=True)

    # def __str__(self) -> str:
    #     return f"{self.first_name} {self.last_name}"


# class Gallery(models.Model):
    # image = models.ImageField(upload_to=)

