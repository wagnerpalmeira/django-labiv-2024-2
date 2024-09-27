from django.db import models
from django.contrib.auth import get_user_model
from .promotion import Promotion

user_model = get_user_model()

class Comment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    user = models.ForeignKey(user_model, on_delete=models.PROTECT)
    promotion = models.ForeignKey(Promotion, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title
