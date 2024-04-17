from django.db import models
from django.conf import settings

# Create your models here.


class Frase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    texto = models.TextField(max_length=200)
    autor = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
