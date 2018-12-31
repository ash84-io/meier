# -*- coding:utf-8 -*-
import logging
from logging import Formatter
from logging import StreamHandler

logger = logging.getLogger("meier_app.logger")
logging.basicConfig()
stream_handler = StreamHandler()
log_formatter = Formatter(
    "[%(process)d:%(processName)s:%(thread)d:%(threadName)s] %(asctime)s : %(message)s [in %(filename)s:%(lineno)d]"
)
stream_handler.setFormatter(log_formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)
