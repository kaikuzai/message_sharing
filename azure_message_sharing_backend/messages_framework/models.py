from django.db import models

# Create your models here.
class Messagedata(models.Model):
    message_id = models.IntegerField(null=False, blank=False, unique=True)
    author = models.CharField(max_length=100)
    anonymous = models.BooleanField()
    message = models.TextField(blank=False, null=False)
    rating = models.FloatField()