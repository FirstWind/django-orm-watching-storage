import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": "checkpoint.devman.org",
        "PORT": "5434",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
    }
}

INSTALLED_APPS = ["datacenter"]

SECRET_KEY = ""

DEBUG = True

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = []


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
    },
]


USE_L10N = True

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Asia/Chita"

USE_TZ = True
