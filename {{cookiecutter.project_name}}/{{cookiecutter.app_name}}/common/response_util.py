# -*- coding: UTF-8 -*-
"""
    请求响应的拼装
"""

import math
from {{cookiecutter.app_name}}.consts import res_status


def response_body(data, status=res_status.OK):
    body = {"status": status, "data": data}
    return body


def paginate_body(items, total, page, per_page):
    result = dict()
    result['total'] = math.ceil(float(total / per_page))
    result['has_more'] = 1 if page * per_page < total else 0
    result["query"] = [x.serialize() for x in items]
    return result


def query_body(items):
    result = dict()
    result['query'] = [x.serialize() for x in items]
    return result
