# meier : Self-Hosted Blog Platform For Developer

[![Build Status](https://travis-ci.org/meier-project/meier.svg?branch=master)](https://travis-ci.org/meier-project/meier)

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