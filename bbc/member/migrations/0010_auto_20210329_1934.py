# Generated by Django 3.0.5 on 2021-03-29 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_remove_groupmember_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='count',
        ),
        migrations.AddField(
            model_name='group',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]