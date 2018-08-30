# meier
### self-hosted blog platform

[![Build Status](https://travis-ci.org/meier-project/meier.svg?branch=master)](https://travis-ci.org/meier-project/meier)
[![https://img.shields.io/github/contributors/meier-project/meier.svg](https://github.com/meier-project/meier/graphs/contributors)

### Install

```shell
pip3 install -r ./requirements
```

#### Requirements

- Python3.6
- Linus/Unix Server

### Run

```shell
gunicorn meier:app -c config.ini
```