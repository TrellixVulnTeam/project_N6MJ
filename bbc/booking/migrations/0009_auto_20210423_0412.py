# Generated by Django 3.0.5 on 2021-04-22 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_auto_20210423_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allcourtinfo',
            name='groupbooking_lastmonth_duration',
            field=models.PositiveIntegerField(null=True),
        ),
    ]