# Generated by Django 4.2.4 on 2023-09-03 07:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sub_task', '0002_alter_sudtask_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudtask',
            name='complete_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sudtask',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sudtask',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4a6c1edf-7c2c-4c26-aee1-02a7cb0bcea7'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sudtask',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
