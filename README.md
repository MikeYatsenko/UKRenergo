### Requirements

celery (4.4.1)
Django (3.0.4)
django-celery (3.3.1)
django-celery-beat (2.0.0)
kombu (4.6.8)
redis (3.4.1)

### Database
```
ENGINE: 'django.db.backends.postgresql_psycopg2'
NAME: 'ukrenergo'
USER : ''
PASSWORD: ''
HOST: 'localhost'
PORT : '5432'
```

### Usage

Enter commands in the terminal to run app
```
$ python manage.py makemigrations
$ python manage.py migrate
```
You need to create super user to have an access to the admin panel, and after that in admin panel (localhost/admin) you also need to create User to fill up a URL data 
```
$ python manage.py createsuperuser
$ python manage.py runserver
```

Run redis server 
```
$ redis-server
```

In another terminal enter 
```
$ celery -A usite  worker --beat --scheduler django --loglevel=info

```

