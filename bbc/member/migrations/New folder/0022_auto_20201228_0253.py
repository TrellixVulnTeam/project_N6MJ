# Generated by Django 3.0.5 on 2020-12-27 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0021_auto_20201228_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='group_role',
        ),
        migrations.RemoveField(
            model_name='member',
            name='mygroup',
        ),
    ]
