from rest_framework import serializers
from .models import SudTask


class SudTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudTask
        fields = [
            'id',
            'task_id',
            'team',
            'is_complete',
            'complete_date',
            'created_date',
            'updated_date',
        ]