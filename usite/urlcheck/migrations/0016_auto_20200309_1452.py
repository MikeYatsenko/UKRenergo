# Generated by Django 3.0.4 on 2020-03-09 19:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('urlcheck', '0015_auto_20200307_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 9, 19, 52, 14, 714075, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='url',
            name='response_code',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='url',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 9, 19, 52, 14, 714099, tzinfo=utc)),
        ),
    ]
