import os

import environ

env = environ.Env(
    DEBUG=(bool, False)
    )
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env.read_env(os.path.join(BASE_DIR, ".env"))

DATABASES = {"default": env.db()}

SECRET_KEY = env("DATABASE_SECRET_KEY")

DEBUG = env("DEBUG")

INSTALLED_APPS = ["datacenter"]

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

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
