FROM python:3.11-slim

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use prod settings by default inside container
ENV DJANGO_SETTINGS_MODULE=mmm_ui.settings.prod

# Collect static files using prod settings
RUN python manage.py collectstatic --noinput

# Run with Gunicorn for production
CMD ["gunicorn", "mmm_ui.wsgi:application", "--bind", "0.0.0.0:8001"]
