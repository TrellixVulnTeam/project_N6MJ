# Generated by Django 3.0.5 on 2021-03-14 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20210314_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='court',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='court_num', to='booking.CourtDetail'),
        ),
    ]