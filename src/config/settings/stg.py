from config.settings.base import *  # NOQA

DEBUG = False

SECRET_KEY = "django-insecure-ez9qzqkzj&#a)vdwyapk=4*@&ota68i63a2gcc#e=7ek6gk_ma"

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

STATIC_URL = "static/"
