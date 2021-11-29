import os

from environs import Env

env = Env()
env.read_env()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": "checkpoint.devman.org",
        "PORT": env.str("DATABASE_PORT"),
        "NAME": "checkpoint",
        "USER": env.str("DATABASE_USER"),
        "PASSWORD": env.str("DATABASE_PASSWORD")
    }
}

SECRET_KEY = env.str("DATABASE_SECRET_KEY")

INSTALLED_APPS = ["datacenter"]

DEBUG = env.bool("STATES_DATABASE_DEBUG")

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
