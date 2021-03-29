# Generated by Django 3.0.5 on 2021-03-27 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20210328_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.IntegerField(default=None)),
                ('state', models.BooleanField(default=False)),
                ('count', models.IntegerField(default=0)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Group')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
            options={
                'db_table': 'request_member',
            },
        ),
    ]