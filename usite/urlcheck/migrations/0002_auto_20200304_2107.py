# Generated by Django 3.0.4 on 2020-03-04 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlcheck', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='url',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='url',
            name='interval',
            field=models.DurationField(default=datetime.timedelta(0, 60)),
        ),
        migrations.AlterField(
            model_name='url',
            name='response_code',
            field=models.CharField(max_length=4),
        ),
    ]
