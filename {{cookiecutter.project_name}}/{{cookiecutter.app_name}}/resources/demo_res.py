# -*- coding: UTF-8 -*-
"""
    demo api
"""

from flask_restful import Resource, reqparse
from {{cookiecutter.app_name}}.consts.res_status import OK, ERROR
from {{cookiecutter.app_name}}.consts.tips import REQUEST_ARG_REQUIRED
from {{cookiecutter.app_name}}.common.response_util import response_body
from {{cookiecutter.app_name}}.handler.demo_handler import query_by_id


class DemoAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(DemoAPI, self).__init__()

    def get(self):
        self.reqparse.add_argument('id', required=True, type=str, help=REQUEST_ARG_REQUIRED.format('id'), location='args')
        args = self.reqparse.parse_args()
        id = args.get('id')
        result = query_by_id(id)
        if result:
            return response_body(result, OK)
        else:
            return response_body('Internal Error', ERROR), 500
    
    def post(self):
        pass

    def put(self):
        pass
    
    def delete(self):
        pass
