# Generated by Django 3.0.5 on 2021-05-17 15:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0028_auto_20210516_0441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allcourtinfo',
            old_name='ads',
            new_name='contacts',
        ),
        migrations.AlterField(
            model_name='booking',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 17, 22, 20, 25, 960694, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 17, 22, 20, 25, 961724, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 17, 22, 20, 25, 962722, tzinfo=utc)),
        ),
    ]