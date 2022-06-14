from django.db import models
from .myModels import bs
# Create your models here.
class rsa(models.Model):
    p = models.IntegerField()
    q = models.IntegerField()
    a = models.IntegerField()
    n = models.IntegerField()
    phi = models.IntegerField()
    b = models.IntegerField()
    