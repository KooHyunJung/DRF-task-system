# Generated by Django 4.2.4 on 2023-09-03 07:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_id_alter_task_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.UUIDField(default=uuid.UUID('23f356c9-3130-4353-9989-1cdf0212f5e8'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
