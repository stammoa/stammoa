from django.db import models

# Create your models here.
class CouponList(models.Model):
    cafeName = models.CharField(max_length=30)
    description = models.CharField(max_length=50)