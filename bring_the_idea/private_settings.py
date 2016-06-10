import os

SECRET_KEY = "1"

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("POSTGRES_DB"),
        'USER': "postgres",
        'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
        'HOST': 'db',
        'PORT': '5432',
    }
}

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "btidb",
        'USER': "grigoriy",
        'PASSWORD': "Gregornet123",
        'HOST': '',
        'PORT': '',
    }
}

services:
  db:
    image: postgres:9.4
    environment:
      POSTGRES_PASSWORD: 'secret'
      POSTGRES_DB: 'demo'
    volumes:
      - /var/lib/postgresql/data
"""
