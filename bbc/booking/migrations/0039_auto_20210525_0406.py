# Generated by Django 3.0.5 on 2021-05-24 21:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0038_auto_20210525_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allcourtinfo',
            name='bank_acc_id',
        ),
        migrations.RemoveField(
            model_name='allcourtinfo',
            name='bank_acc_name',
        ),
        migrations.RemoveField(
            model_name='allcourtinfo',
            name='refund_group_percent',
        ),
        migrations.RemoveField(
            model_name='allcourtinfo',
            name='refund_member_percent',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_pic',
        ),
        migrations.AlterField(
            model_name='booking',
            name='refund_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 25, 4, 6, 17, 989650, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 25, 4, 6, 17, 989650, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 25, 4, 6, 17, 990650, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 25, 4, 6, 17, 990650, tzinfo=utc)),
        ),
    ]
