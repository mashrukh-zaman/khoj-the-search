from django.db import models
from uuid import uuid4

# Create your models here.
class Value(models.Model):
    input_value = models.CharField(max_length=100)
    search_value = models.CharField(max_length=100)
    user_id = models.IntegerField(default=0)
    # user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)