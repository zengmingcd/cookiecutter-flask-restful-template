# -*- coding: UTF-8 -*-
"""
    demo 业务逻辑函数
"""

from flask_restful import current_app
from {{cookiecutter.app_name}}.models.models import DemoModel

def query_by_id(id):
    result = None
    if id:
        my_app = current_app
        with my_app.app_context() as appc:
            demo_obj = DemoModel.query.filter_by(id=id).first()
            if demo_obj:
                result = demo_obj.serialize()
            db.session.close()
    return result

