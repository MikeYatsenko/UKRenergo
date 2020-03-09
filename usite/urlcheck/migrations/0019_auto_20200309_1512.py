# Generated by Django 3.0.4 on 2020-03-09 20:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('urlcheck', '0018_auto_20200309_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='url',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
