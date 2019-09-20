FROM python:3.7.3-slim-stretch
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
ENTRYPOINT ["gunicorn"]
CMD ["wsgi:app", "-c" , "config.ini"]