# Generated by Django 3.0.5 on 2020-12-23 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20201224_0239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='group_name',
            new_name='mygroup',
        ),
    ]