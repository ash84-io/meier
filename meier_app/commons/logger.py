# -*- coding:utf-8 -*-
import logging
from logging import Formatter
from logging import FileHandler, StreamHandler
from flask import current_app
logger = logging.getLogger('meier_app.logger')
logging.basicConfig()
stream_handler = StreamHandler()
log_formatter = Formatter("[%(process)d:%(processName)s:%(thread)d:%(threadName)s] %(asctime)s : %(message)s [in %(filename)s:%(lineno)d]")
if current_app.testing:
    log_file_handler = FileHandler(filename="./log/meier.log", mode='a', encoding="utf-8")
    logger.addHandler(log_file_handler)
    log_file_handler.setFormatter(log_formatter)
stream_handler.setFormatter(log_formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)