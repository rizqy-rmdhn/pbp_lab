from django.db import models

# Create your models here.
class Task(models.Model):
    date = models.DateField(auto_now="True")
    title = models.CharField(max_length=255)
    description = models.TextField()