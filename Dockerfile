FROM python:3.7.3-alpine3.9
RUN pip install -U pip

RUN apk update && apk add --no-cache --upgrade \
    build-base \
    gcc \
    libxml2-dev \
    g++ \
    python-dev \
    libxslt-dev




WORKDIR /wheels
COPY requirements.txt .

RUN pip install -r requirements.txt


ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY meier meier
COPY config.ini config.ini
COPY wsgi.py wsgi.py
RUN ls -al
ENTRYPOINT ["gunicorn"]
CMD ["wsgi:app", "-c" , "config.ini"]
