# Generated by Django 3.0.4 on 2020-03-07 19:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('urlcheck', '0014_auto_20200307_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 7, 19, 12, 24, 728316, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='url',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 7, 19, 12, 24, 728342, tzinfo=utc)),
        ),
    ]
