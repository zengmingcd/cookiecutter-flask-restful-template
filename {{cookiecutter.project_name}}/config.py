# -*- coding: UTF-8 -*-

"""
    配置文件
"""

import os
import logging
from logging import StreamHandler
from logging.handlers import TimedRotatingFileHandler

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        # 初始化日志
        app.logger.setLevel(logging.INFO)

        log_file_name = r'{{cookiecutter.app_name}}.log'
        log_format = r'[%(levelname)-5s] %(asctime)s %(filename)s[%(lineno)s]:%(funcName)s - %(message)s'
        # 文件日志
        log_path = os.path.join(basedir, r'logs')
        if not os.path.exists(log_path):
            os.makedir(log_path)
        log_file = os.path.join(log_path, log_file_name)
        log_file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1)
        log_file_handler.setFormatter(logging.Formatter(log_format))
        log_file_handler.setLevel(logging.INFO)
        app.logger.addHandler(log_file_handler)

        # 控制台日志
        log_console_handler = StreamHandler()
        log_console_handler.setFormatter(logging.Formatter(log_format))
        log_console_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(log_console_handler)

class DevelopmentConfig(Config):
    DEBUG = True
    USE_RELOAD = False
    SQLALCHEMY_DATABASE_URI = r'mysql://user:password@host:port/schema?charset=utf8'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = r'mysql://user:password@host:port/schema?charset=utf8'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
