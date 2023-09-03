import uuid

from django.db import models


class SudTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    team = models.CharField(max_length=30)
    is_complete = models.BooleanField(default=False)
    complete_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
