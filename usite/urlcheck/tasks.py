import celery
import requests

from .models import URL


@celery.task()
def test():
    for row in URL.objects.active():
        try:
            result = requests.get(row['site_url'])
            URL.objects.filter(id=row['id']).update(response_code=result.status_code)
        except:
            print('Wrong url')
            URL.objects.filter(id=row['id']).update(response_code='Error')
            pass
