from .base import *


DEBUG = os.getenv("DEBUG", "False") == "True"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST", "db"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = ["www.managemindmoney.com", "api.managemindmoney.com", "admin.managemindmoney.com"]