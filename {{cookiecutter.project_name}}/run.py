# -*- coding: UTF-8 -*-
"""
    服务启动入口
"""

import os
from app_main import create_app

{{cookiecutter.project_name}} = create_app(os.getenv(r'{{cookiecutter.project_name}}_CONFIG') or r'default')

if __name__ == '__main__':
    {{cookiecutter.project_name}}.logger.info('System Start! Config:')
    {{cookiecutter.project_name}}.logger.info('[Debug]:{}'.format({{cookiecutter.project_name}}.config['DEBUG']))
    {{cookiecutter.project_name}}.logger.info('[Database]:\n\t[SQLALCHEMY_DATABASE_URI]:{}\n\t[SQLALCHEMY_TRACK_MODIFICATIONS]:{}'
                                                .format({{cookiecutter.project_name}}.config['SQLALCHEMY_DATABASE_URI'],
                                                        {{cookiecutter.project_name}}.config['SQLALCHEMY_TRACK_MODIFICATIONS']))
    {{cookiecutter.project_name}}.run('0.0.0.0')
