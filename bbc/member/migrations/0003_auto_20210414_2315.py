# Generated by Django 3.0.5 on 2021-04-14 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20210411_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='member.Member'),
        ),
        migrations.AlterField(
            model_name='request',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='member.Member'),
        ),
    ]
