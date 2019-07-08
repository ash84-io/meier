# meier
### self-hosted blog platform

[![Build Status](https://travis-ci.org/meier-project/meier.svg?branch=master)](https://travis-ci.org/meier-project/meier)

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
docker run -p 80:2368 --env-file .env meier:1.0.0 
```

### Version

- v1.0.0
