import uuid

from django.db import models
from rest_framework.exceptions import ValidationError

TEAM_LIST = [
    '단비',
    '다래',
    '블라블라',
    '철로',
    '땅이',
    '해태',
    '수피',
]


def validate_team_list(value):
    for item in value.split(','):
        if item.strip() not in TEAM_LIST:
            raise ValidationError(f"'{item}' is not a valid team name.")


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), unique=True)
    user_id = models.IntegerField()
    team = models.CharField(max_length=200, validators=[validate_team_list])
    # team = models.ListField(models.CharField(max_length=30), default=list, validators=[validate_team_list])
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    is_complete = models.BooleanField(default=False)
    complete_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
