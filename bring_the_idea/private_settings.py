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

ADMINS = [
    ("admin", "admin@test.com", "admin"), # username, email, initial password
]
