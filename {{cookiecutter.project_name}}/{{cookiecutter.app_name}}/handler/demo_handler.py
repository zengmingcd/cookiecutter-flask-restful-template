# -*- coding: UTF-8 -*-
"""
    demo 业务逻辑函数
"""

from flask_restful import current_app
from extensions import db
from {{cookiecutter.app_name}}.models.models import DemoModel


def query_by_id(d_id):
    result = None
    if d_id:
        my_app = current_app
        with my_app.app_context() as appc:
            demo_obj = DemoModel.query.filter_by(id=d_id).first()
            if demo_obj:
                result = demo_obj.serialize()
                my_app.logger.info(r'search success')
            db.session.close()
    return result

