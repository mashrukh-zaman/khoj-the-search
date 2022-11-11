from django.db import models

# Create your models here.
class Value(models.Model):
    input_value = models.CharField(max_length=100)
    search_value = models.CharField(max_length=100)