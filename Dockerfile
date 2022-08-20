FROM python:3.10.6-slim-buster as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


# final stage
FROM python:3.10.6-slim

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
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

# Set Environment Variables for applicatin
ENV DB_HOST=$DB_HOST
ENV DB_USER=$DB_USER
ENV DB_NAME=$DB_NAME
ENV DB_HOST=$DB_HOST
ENV DB_PASSWORD=$DB_PASSWORD
ENV SENTRY_DSN=$SENTRY_DSN

ENTRYPOINT ["gunicorn"]
CMD ["wsgi:app", "-c" , "config.ini"]


