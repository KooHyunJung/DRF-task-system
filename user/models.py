from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    team = models.CharField(max_length=30)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
