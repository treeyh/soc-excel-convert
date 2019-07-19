#-*- encoding: utf-8 -*-

import json
from datetime import date, datetime


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def json_encode(obj):
    return json.dumps(obj, cls = JsonEncoder)


def json_decode(value):
    return json.loads(value)