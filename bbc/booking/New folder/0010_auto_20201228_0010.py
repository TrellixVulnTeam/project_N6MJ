# Generated by Django 3.0.5 on 2020-12-27 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0014_auto_20201227_0633'),
        ('booking', '0009_auto_20201225_0401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refund',
            name='history',
        ),
        migrations.AddField(
            model_name='refund',
            name='history_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.HistoryGroup'),
        ),
        migrations.AddField(
            model_name='refund',
            name='history_member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.HistoryMember'),
        ),
        migrations.AlterField(
            model_name='historygroup',
            name='header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_group', to='member.Group'),
        ),
        migrations.AlterField(
            model_name='historymember',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_member', to='member.Member'),
        ),
    ]