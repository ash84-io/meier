# Meier [![Build Status](https://travis-ci.org/meier-project/meier.svg?branch=master)](https://travis-ci.org/meier-project/meier)

self-hosted blog platform

### Tech

- Backend
    - python3.6
    - flask
    - gunicorn

- Frontend
    - material-kit
    - [axios](https://github.com/axios/axios)
    - vue.js

### Run

```shell
gunicorn meier:app -c config.ini
```