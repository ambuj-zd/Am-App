# Generated by Django 4.1.7 on 2023-02-21 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_name_task_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='userid',
            new_name='name',
        ),
    ]