# -*- coding: UTF-8 -*-
"""
    数据库模型
"""

import datetime
from {{cookiecutter.project_name}}.extensions import db

class DemoModel(db.Model):
    """
        demo模型
    """
    __tablename__ = r'demo_model'
    id = db.Column(r'id', db.Integer, primary_key=True, comment=r'主键id')
    name = db.Column(r'name', db.String(50), nullable=False, default=r'ming', comment=r'姓名')
    age = db.Column(r'age', db.Integer, nullable=False, default='18', comment=r'年龄')
    create_time = db.Column(r'create_time', db.DateTime, default=datetime.datetime.now, nullable=False, comment=r'创建时间')

    def __repr__(self):
        return '<id {}; name {}; age {}>'.format(self.id, self.name, self.age)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S')
        }

