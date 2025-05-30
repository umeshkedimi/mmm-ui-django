from .base import *

DEBUG = os.getenv("DEBUG", "True") == "True"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATICFILES_DIRS = [BASE_DIR / "main" / "static"]

SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-dev-key")

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"