FROM python:3.10.6-slim-buster as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# final stage
FROM python:3.10.6-slim

WORKDIR /app

COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/*

COPY meier meier
COPY config.ini config.ini
COPY wsgi.py wsgi.py

# Get Arguments
ARG DB_HOST
ARG DB_USER
ARG DB_NAME
ARG DB_PASSWORD
ARG SENTRY_DSN

# Set Environment Variables for application
ENV DB_HOST=$DB_HOST \
    DB_USER=$DB_USER \
    DB_NAME=$DB_NAME \
    DB_PASSWORD=$DB_PASSWORD \
    SENTRY_DSN=$SENTRY_DSN

ENTRYPOINT ["gunicorn"]
CMD ["wsgi:app", "-c", "config.ini"]
