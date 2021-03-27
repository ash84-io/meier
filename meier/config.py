import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    sentry_dsn = os.getenv("SENTRY_DSN")
