# Dj-Blog
A Mini blog with Python Django Framework
### Creating Virtual Environment for flexibility
```sh
$ apt install python-virtualenv python-pip python-dev 
$ source Dj-Blog/python/venv_django/bin/activate
$ pip install Dj-Blog/requirements.txt
```
### Install Database Pstgresql 

```sh
$ apt-get install  postgresql postgresql-contrib libpq-dev
$ sudo su postgres
$ psql
```
  Create Db and Db user and set roles
```sh
$ CREATE DATABASE dj;
$ CREATE USER admin_dj WITH PASSWORD 'test1234.';
$ ALTER ROLE admin_dj SET client_encoding TO 'utf8';
$ ALTER ROLE admin_dj SET default_transaction_isolation TO 'read committed';
$ ALTER ROLE admin_dj SET timezone TO 'UTC';
$ GRANT ALL PRIVILEGES ON DATABASE dj TO admin_dj;
```
You Can change your custom Postgres admin and user settings  under python/Blog/Blog/seetings.py 
```sh

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dj',
        'USER': 'admin_dj',
        'PASSWORD': 'test1234.',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
```
After creating virtual env and psql Db you can migration
```sh
$ python Dj-Blog/python/Blog/manage.py makemigrations
$ python  Dj-Blog/python/Blog/manage.py migrate
```
if all things is done with no error you can add for site management user
```sh
$ python Dj-Blog/python/Blog/manage.py createsuperuser
```
Finally run the server for all interfaces
```sh
$ python Dj-Blog/python/Blog/manage.py runserver 0.0.0.0:8000
```



