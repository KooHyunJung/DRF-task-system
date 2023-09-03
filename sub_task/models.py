from django.db import models

from task.models import validate_team_list


class SudTask(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField()
    team = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
    complete_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
