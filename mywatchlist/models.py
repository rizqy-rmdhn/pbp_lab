from turtle import title
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class MyWatchList(models.Model):
    WATHCED_STATUS = [
        (0, "not watched"),
        (1, "watched")
    ]
    
    watched = models.IntegerField(choices=WATHCED_STATUS)
    title = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(5)])
    release_date = models.DateField()
    revview = models.TextField()