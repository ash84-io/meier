# -*- coding:utf-8 -*-
import os
import sys
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
from meier_app.app import create_app
app = create_app('meier_app.config.ProductionConfig')