from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20)
    pid = models.IntegerField(null=True)
