# meier
> self-hosted blog platform

![Meier Version: 1.0.1](https://badgen.net/badge/version/1.0.1/orange)
[![Build Status](https://travis-ci.org/meier-project/meier.svg?branch=develop)](https://travis-ci.org/meier-project/meier)
[![Python Version: 3.7](https://badgen.net/badge/python/3.7/blue)](https://docs.python.org/3.7/)
[![Code Style: Black](https://badgen.net/badge/code%20style/black/black)](https://github.com/ambv/black)


### ENV(.env)
```
DB_HOST=localhost:3306
DB_NAME=meier
DB_USER=
DB_PASSWORD=
SENTRY_DSN=
```

### Run

```shell
docker run -p 80:2368 -v ~/themes:/app/meier/templates/themes -d --env-file .env me
ier:{{version}} 
```
