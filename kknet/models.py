from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.hashers import make_password, check_password



# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Icecream(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField("")
    mfr = models.CharField(max_length=100)
    category = models.ForeignKey(max_length=100)
    img = models.CharField(max_length=100)
    
class Review(models.Model):
    rating = models.IntegerField(validators= [MinValueValidator(0), MaxValueValidator(5)])
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    pw_hash = models.CharField(max_length=128)
    ice_cream = models.ForeignKey("Icecream")
    
    
    
class Discountinfo(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    pw_hash = models.CharField(max_length=128)
    ice_cream = models.ForeignKey("Icecream")





