from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()

class Promotion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    url = models.URLField() 

    user = models.ForeignKey(user_model, on_delete=models.PROTECT)

class Comment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    user = models.ForeignKey(user_model, on_delete=models.PROTECT)
    promotion = models.ForeignKey(Promotion, on_delete=models.PROTECT)
