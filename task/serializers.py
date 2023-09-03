from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'user_id',
            'team',
            'title',
            'content',
            'is_complete',
            'complete_date',
            'created_date',
            'updated_date',
        ]
