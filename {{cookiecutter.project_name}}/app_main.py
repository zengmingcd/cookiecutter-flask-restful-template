# -*- coding: UTF-8 -*-
"""
    app入口
"""

from flask import Flask
from config import config
from extensions import db

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from {{cookiecutter.app_name}}.resources_register import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/{{cookiecutter.project_name}}')

    return app
