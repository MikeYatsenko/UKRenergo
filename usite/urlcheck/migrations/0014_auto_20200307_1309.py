# Generated by Django 3.0.4 on 2020-03-07 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlcheck', '0013_auto_20200305_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(blank=True, default='2020-03-07 13:09:04'),
        ),
        migrations.AlterField(
            model_name='url',
            name='updated_at',
            field=models.DateTimeField(blank=True, default='2020-03-07 13:09:04'),
        ),
    ]
