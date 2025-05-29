# Dockerfile for MMM Django UI
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project
COPY . .

# Expose Django port
EXPOSE 8001

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
