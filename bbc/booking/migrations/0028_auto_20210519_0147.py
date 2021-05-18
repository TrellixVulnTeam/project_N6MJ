# Generated by Django 3.0.5 on 2021-05-18 18:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0027_auto_20210514_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 19, 1, 47, 31, 663964, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 19, 1, 47, 31, 664596, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 19, 1, 47, 31, 666378, tzinfo=utc)),
        ),
    ]