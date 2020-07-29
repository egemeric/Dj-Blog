# Dj-Blog
A Mini blog with Python Django Framework
### Creating Virtual Environment 
```sh
$ sudo apt install python-virtualenv
$ cd Dj-Blog/python
$ python3 -m venv dj_venv
$ source dj_venv/bin/activate
$ pip install --upgrade pip
$ pip install -r Dj-Blog/requirements.txt
```
If you dont want work on virt env just intall django and postgres connector via pip
```sh
$ pip install --upgrade pip
$ pip install -r requirements.txt
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
[Style and About the Dj-Blog](https://github.com/egemeric/Dj-Blog/blob/master/python/README.md)


