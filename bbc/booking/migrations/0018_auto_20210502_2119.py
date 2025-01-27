# Generated by Django 3.0.5 on 2021-05-02 14:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_auto_20210502_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(
                2021, 5, 2, 21, 19, 34, 528073, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(
                2021, 5, 2, 21, 19, 34, 529105, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(
                2021, 5, 2, 21, 19, 34, 530100, tzinfo=utc)),
        ),
    ]
