# Generated by Django 4.1.1 on 2022-09-13 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_remove_task_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='text',
        ),
    ]
