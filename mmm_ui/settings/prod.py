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

STATIC_URL = "/static/"

# This should only be used in production
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = ["www.managemindmoney.com", "api.managemindmoney.com", "admin.managemindmoney.com"]