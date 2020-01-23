# meier
> self-hosted blog platform

[![Code Style: Black](https://badgen.net/badge/code%20style/black/black)](https://github.com/ambv/black)
[![codecov](https://codecov.io/gh/meier-project/meier/branch/develop/graph/badge.svg)](https://codecov.io/gh/meier-project/meier)
![GITHUB-ACTION-CI](https://github.com/meier-project/meier/workflows/CI/badge.svg)

### ENV(.env)
```
DB_HOST=localhost:3306
DB_NAME=meier
DB_USER=root
DB_PASSWORD=root
SENTRY_DSN=http://setnry-dsn
```

### Run

```shell
docker run -p 80:2368 -v ~/themes:/app/meier/templates/themes -d --env-file .env me
ier:{{version}} 
```
