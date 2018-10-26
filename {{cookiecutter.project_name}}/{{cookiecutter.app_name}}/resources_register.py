# -*- coding: UTF-8 -*-
"""
    资源入口
"""

from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS
from {{cookiecutter.app_name}}.resources.demo_res import DemoAPI

api_blueprint = Blueprint('api_blueprint', __name__)
CORS(api_blueprint, supports_credentials=True)
api = Api(api_blueprint)

api.add_resource(DemoAPI, '/demo')
