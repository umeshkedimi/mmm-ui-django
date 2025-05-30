FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . /app

# Copy the production .env file into container
COPY .env /app/.env

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files using prod settings
ENV DJANGO_SETTINGS_MODULE=mmm_ui.settings
ENV DJANGO_ENV=prod

RUN python manage.py collectstatic --noinput

# Run with Gunicorn in production
CMD ["gunicorn", "mmm_ui.wsgi:application", "--bind", "0.0.0.0:8001"]
