from django.conf import settings
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class Categories(models.Model):
    brand = models.CharField(max_length=255)
    image = models.ImageField(upload_to="category_images/", blank=True, null=True)
    excerpt = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.brand}'

class Seller(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=15)
    address = models.CharField(max_length=255, null=True, blank=True)
    liked_cars = models.ManyToManyField('Cars', blank=True, related_name='liked_by')

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Cars(models.Model):
    image = models.ImageField(upload_to="photos/", null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    slug = AutoSlugField(
        populate_from='name',
        unique=True,
        always_update=False, 
    )
    price = models.IntegerField()
    excerpt = models.CharField(max_length=200, null=True)
    content = models.TextField()
    date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.slug