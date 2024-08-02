from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Icecream(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField("")
    mfr = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    
    
class Review(models.Model):
    rating = models.IntegerField(validators= [MinValueValidator(0), MaxValueValidator(5)])
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    pw_hash = models.CharField(max_length=128)
    ice_cream = models.ForeignKey(Icecream, on_delete=models.CASCADE, related_name="reviews")
    
    
class Discountinfo(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    pw_hash = models.CharField(max_length=128)
    ice_cream = models.ForeignKey(Icecream, on_delete=models.CASCADE, related_name= "informations")






