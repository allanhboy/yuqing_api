# -*- coding: utf-8 -*-

import six

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'



validators = {
    ('articles', 'GET'): {'args': {'required': [], 'properties': {'page_index': {'type': 'integer'}, 'follow_type': {'type': 'integer'}}}},
    ('wechat_login', 'POST'): {'json': {'type': 'object', 'properties': {'code': {'type': 'string', 'description': '调用接口wx.login() 获取临时登录凭证（code）'}, 'random': {'type': 'string', 'description': '小程序客户端随机生成6位数字'}}}},
    ('newfollow', 'POST'): {'json': {'type': 'object', 'properties': {'company_name': {'type': 'string'}, 'short_name': {'type': 'string'}}}},
    ('account_login', 'POST'): {'json': {'type': 'object', 'properties': {'password': {'type': 'string'}, 'username': {'type': 'string'}}}},
    ('follow', 'POST'): {'json': {'type': 'object', 'properties': {'follow_type': {'type': 'integer', 'enum': [1, 2]}, 'id': {'type': 'integer'}}}},
    ('follow', 'DELETE'): {'json': {'type': 'object', 'properties': {'follow_type': {'type': 'integer', 'enum': [1, 2]}, 'id': {'type': 'integer'}}}},
    ('search', 'GET'): {'args': {'required': [], 'properties': {'follow_type': {'type': 'integer', 'enum': [1, 2]}, 'key': {'type': 'integer'}}}},
}

filters = {
    ('article_id', 'GET'): {200: {'schema': {'type': 'object', 'properties': {"follow_type'": {'type': 'integer'}, 'source_url': {'type': 'string'}, 'content': {'type': 'string'}, 'source': {'type': 'string'}, 'follow_name': {'type': 'string'}, 'title': {'type': 'string'}, 'id': {'type': 'integer'}}}, 'headers': None}},
    ('articles', 'GET'): {200: {'schema': {'type': 'object', 'properties': {'articles': {'type': 'array', 'items': {'type': 'object', 'properties': {'is_read': {'type': 'integer'}, "follow_type'": {'type': 'integer', 'enum': [1, 2]}, 'time': {'type': 'string'}, 'follow_name': {'type': 'string'}, 'title': {'type': 'string'}, 'id': {'type': 'integer'}}}}}}, 'headers': None}},
    ('wechat_login', 'POST'): {200: {'schema': {'type': 'object', 'properties': {'session': {'type': 'string', 'description': '小程序登录凭证,对应表session.id'}, 'expire_time': {'type': 'string', 'description': '对应表session.expire_time'}, 'is_binding': {'type': 'boolean', 'description': 'openid在表employee找不到返回False,否则为True'}}}, 'headers': None}},
    ('newfollow', 'POST'): {400: {'schema': None, 'headers': None}, 204: {'schema': None, 'headers': None}},
    ('article_id_invalid', 'PUT'): {204: {'schema': None, 'headers': None}},
    ('account_login', 'POST'): {400: {'schema': None, 'headers': None}, 204: {'schema': None, 'headers': None}},
    ('follows', 'GET'): {200: {'schema': {'type': 'object', 'properties': {'company': {'type': 'array', 'items': {'type': 'object', 'properties': {'company_name': {'type': 'string'}, 'short_name': {'type': 'integer'}, 'id': {'type': 'integer'}}}}, 'industry': {'type': 'array', 'items': {'type': 'object', 'properties': {'industry_name': {'type': 'string'}, 'children_count': {'type': 'integer'}, 'id': {'type': 'integer'}}}}}}, 'headers': None}},
    ('follow', 'POST'): {204: {'schema': None, 'headers': None}},
    ('follow', 'DELETE'): {204: {'schema': None, 'headers': None}},
    ('home', 'GET'): {200: {'schema': {'type': 'object', 'properties': {'new_company_news': {'type': 'integer'}, 'new_industry_news': {'type': 'integer'}, 'articles': {'type': 'array', 'items': {'type': 'object', 'properties': {'is_read': {'type': 'integer'}, 'time': {'type': 'string'}, 'follow_name': {'type': 'string'}, 'follow_type': {'type': 'integer', 'enum': [1, 2]}, 'title': {'type': 'string'}, 'id': {'type': 'integer'}}}}, 'employee': {'type': 'object', 'properties': {'picture': {'type': 'string'}, 'realname': {'type': 'string'}}}}}, 'headers': None}},
    ('search', 'GET'): {200: {'schema': {'type': 'object', 'properties': {'follows': {'type': 'array', 'items': {'type': 'object', 'properties': {'industry_name': {'type': 'string'}, 'children_count': {'type': 'integer'}, 'id': {'type': 'integer'}}}}}}, 'headers': None}},
}

scopes = {
    ('account_login', 'POST'): [],
}


class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None):
    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema is not False:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, dict):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize(schema, data):
        if schema is True or schema == {}:
            return data
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
        }
        type_ = schema.get('type', 'object')
        if type_ not in funcs:
            type_ = 'default'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors
