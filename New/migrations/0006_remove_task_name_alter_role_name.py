# Generated by Django 4.1.7 on 2023-02-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New', '0005_remove_task_userid_task_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]