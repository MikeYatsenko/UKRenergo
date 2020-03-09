import datetime
import pytz

from django.db import models
from usite.settings import DATETIME_FORMAT, TIMEZONE
from django.utils import timezone
from datetime import timedelta


class URLManager(models.Manager):
    def active(self):
        now = datetime.datetime.now(tz=pytz.timezone(TIMEZONE)).strftime(DATETIME_FORMAT)
        ids = []
        for row in self.values():
            datetime_to_update = row['updated_at'] + timedelta(minutes=row['interval'])
            check_date = datetime_to_update.strftime(DATETIME_FORMAT)
            if now > check_date:
                ids.append(row['id'])

        return self.filter(id__in=ids).values()


class URL(models.Model):
    site_name = models.CharField(max_length=100, unique=True,)
    site_url = models.URLField(max_length=200, unique=True, help_text="The URL to be monitored.")
    interval = models.IntegerField(help_text="Interval in minutes.")
    response_code = models.CharField(max_length=7)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)

    objects = URLManager()
