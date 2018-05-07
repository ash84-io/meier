# -*- coding:utf-8 -*-
import logging
from logging import Formatter
from logging import FileHandler, StreamHandler

logger = logging.getLogger('meier_app.logger')
logging.basicConfig()
stream_handler = StreamHandler()
log_file_handler = FileHandler(filename="./log/meier.log", mode='a', encoding="utf-8")
log_formatter = Formatter("[%(process)d:%(processName)s:%(thread)d:%(threadName)s] %(asctime)s : %(message)s [in %(filename)s:%(lineno)d]")
log_file_handler.setFormatter(log_formatter)
stream_handler.setFormatter(log_formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(log_file_handler)
logger.addHandler(stream_handler)