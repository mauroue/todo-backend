# Generated by Django 4.1.1 on 2022-09-07 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_is_compĺeted_task_compĺeted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='compĺeted',
            new_name='completed',
        ),
    ]
