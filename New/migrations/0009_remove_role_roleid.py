# Generated by Django 4.1.7 on 2023-02-23 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('New', '0008_role_id_alter_role_roleid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='roleid',
        ),
    ]
