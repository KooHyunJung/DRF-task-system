from django.db import models


class SudTask(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.CharField(max_length=30)
    is_complete = models.BooleanField(default=False)
    complete_date = models.DateField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
