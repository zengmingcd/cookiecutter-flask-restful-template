# -*- coding: UTF-8 -*-
"""
    项目管理控制台
"""

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app_main import create_app
from extensions import db
from {{cookiecutter.app_name}}.models import models

app = create_app(os.getenv('{{cookiecutter.project_name}}_CONFIG') or 'default')
manage = Manager(app)

migrate = Migrate(app, db)

manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()

    """
        python manage.py db init
        python manage.py db migrate
        python manage.py db upgrade
    """
