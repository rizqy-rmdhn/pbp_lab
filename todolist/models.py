from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    FINISHED_STATUS = [
        (0, "Unfinished"),
        (1, "Finished")
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now="True")
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.IntegerField(default=0, choices=FINISHED_STATUS)
    
    
    