from django.db import models


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(max_length=30)
    team = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    content = models.IntegerField(max_length=500)
    is_complete = models.BooleanField(default=False)
    complete_date = models.DateField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
