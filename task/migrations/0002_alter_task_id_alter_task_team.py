# Generated by Django 4.2.4 on 2023-09-03 06:39

from django.db import migrations, models
import task.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d1e5a66c-beb5-4c24-83e8-fc5aedb14fa3'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='team',
            field=models.CharField(max_length=200, validators=[task.models.validate_team_list]),
        ),
    ]
