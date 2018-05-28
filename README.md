# Meier [![Build Status](https://travis-ci.org/meier-project/meier.svg?branch=master)](https://travis-ci.org/meier-project/meier)

Blog

### Tech

- Backend
    - python3.6
    - flask

- Frontend
    - material-kit
    - [axios](https://github.com/axios/axios)
    - vue.js

### ProdServer Start

```
gunicorn --workers 4 --threads 4 --daemon meier:app -b 0.0.0.0:8080
```

### DevServer Start

```
gunicorn --workers 6--reload meier_dev:app -b 0.0.0.0:8080
```
