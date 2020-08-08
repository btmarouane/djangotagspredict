from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Prediction(models.Model):
    token = models.CharField(max_length=100, primary_key=True)
    title = models.TextField(max_length=100,default="")
    body = models.TextField(max_length=400,default="")
    predicted = models.BooleanField(default=False)
    prediction = models.CharField(max_length=100, default='[]')

    def __str__(self):
        return self.token