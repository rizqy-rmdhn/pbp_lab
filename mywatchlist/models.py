from turtle import title
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class MyWatchList(models.Model):
    NOT_WATHCED_STATUS = 0
    HAVE_WATCHED_STATUS = 1
    WATHCED_STATUS = [
        (NOT_WATHCED_STATUS, "Not watched"),
        (HAVE_WATCHED_STATUS, "Watched")
    ]
    
    watched = models.IntegerField(default=NOT_WATHCED_STATUS, choices=WATHCED_STATUS)
    title = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(5)])
    release_date = models.DateField()
    review = models.TextField()