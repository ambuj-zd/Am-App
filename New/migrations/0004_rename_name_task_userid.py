# Generated by Django 4.1.7 on 2023-02-22 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('New', '0003_rename_userid_task_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='userid',
        ),
    ]
