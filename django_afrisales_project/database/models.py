from django.db import models

# Create your models here.

class Sales(models.Model):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
