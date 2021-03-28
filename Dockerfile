FROM python:3.9.2-slim-buster

RUN pip install -U pip

RUN apt-get update && apt-get install -y build-essential gcc


WORKDIR /wheels
COPY requirements.txt .

RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1

WORKDIR /app

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


