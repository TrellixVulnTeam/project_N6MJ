# Generated by Django 3.0.5 on 2021-04-18 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0010_auto_20210418_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmember',
            name='group',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='member.Group'),
        ),
        migrations.AlterField(
            model_name='request',
            name='group',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Group'),
        ),
    ]