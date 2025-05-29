FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Set environment to production
ENV DJANGO_SETTINGS_MODULE=mmm_ui.settings

# Collect static files inside container
RUN python manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
