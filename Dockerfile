# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim AS build-env

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Create new Django project and configure the settings
RUN python -m django startproject project
RUN cp -r drf_transformers project/drf_transformers
RUN echo "INSTALLED_APPS += ['drf_transformers', 'drf_redesign', 'rest_framework']" >> project/settings.py
RUN echo "from django.urls import include" >> project/urls.py
RUN echo "urlpatterns += [path('', include('drf_transformers.urls')), path('', include('rest_framework.urls'))]" >> project/urls.py

WORKDIR /app
COPY . /app

# Use distroless
FROM gcr.io/distroless/python3
COPY --from=build-env /app /app
WORKDIR /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ai.wsgi"]
