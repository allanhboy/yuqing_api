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


DefinitionsError = {'type': 'object', 'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message']}

validators = {
    ('wechat_login', 'POST'): {'json': {'type': 'object', 'properties': {'random': {'type': 'string', 'description': '小程序客户端随机生成6位数字'}, 'code': {'type': 'string', 'description': '调用接口wx.login() 获取临时登录凭证（code）'}}}},
    ('search', 'GET'): {'args': {'properties': {'type': {'type': 'integer'}, 'key': {'type': 'string'}, 'follow_type': {'enum': [1, 2], 'type': 'integer'}}, 'required': []}},
    ('follow', 'POST'): {'json': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'follow_type': {'type': 'integer', 'enum': [1, 2]}}}},
    ('follow', 'DELETE'): {'json': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'follow_type': {'type': 'integer', 'enum': [1, 2]}}}},
    ('account_login', 'POST'): {'json': {'type': 'object', 'properties': {'username': {'type': 'string'}, 'password': {'type': 'string'}}}},
    ('newfollow', 'POST'): {'json': {'type': 'object', 'properties': {'short_name': {'type': 'string'}, 'company_name': {'type': 'string'}}}},
    ('articles', 'GET'): {'args': {'properties': {'page_index': {'type': 'integer'}, 'follow_type': {'type': 'integer'}, 'key': {'type': 'string'}}, 'required': []}},
}

filters = {
    ('home', 'GET'): {200: {'headers': None, 'schema': {'type': 'object', 'properties': {'employee': {'type': 'object', 'properties': {'picture': {'type': 'string'}, 'realname': {'type': 'string'}}}, 'new_industry_news': {'type': 'integer'}, 'articles': {'type': 'array', 'items': {'type': 'object', 'properties': {'time': {'type': 'string'}, 'id': {'type': 'integer'}, 'is_read': {'type': 'integer'}, 'follow_type': {'type': 'integer', 'enum': [1, 2]}, 'follow_name': {'type': 'string'}, 'title': {'type': 'string'}}}}, 'new_company_news': {'type': 'integer'}}}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
    ('wechat_login', 'POST'): {200: {'headers': None, 'schema': {'type': 'object', 'properties': {'expire_time': {'type': 'string', 'description': '对应表session.expire_time'}, 'is_binding': {'type': 'boolean', 'description': 'openid在表employee找不到返回False,否则为True'}, 'session': {'type': 'string', 'description': '小程序登录凭证,对应表session.id'}}}}, 400: {'headers': None, 'schema': {'type': 'object', 'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message']}}},
    ('article_id', 'GET'): {200: {'headers': None, 'schema': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'content': {'type': 'string'}, 'follow_name': {'type': 'string'}, 'source_url': {'type': 'string'}, 'title': {'type': 'string'}, "follow_type'": {'type': 'integer'}, 'source': {'type': 'string'}}}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
    ('search', 'GET'): {200: {'headers': None, 'schema': {'type': 'object', 'properties': {'follows': {'type': 'array', 'items': {'type': 'object', 'properties': {'short_name': {'type': 'string'}, 'id': {'type': 'integer'}, 'children_count': {'type': 'integer'}, 'follow_type': {'type': 'integer', 'enum': [1, 2]}, 'company_name': {'type': 'string'}, 'industry_name': {'type': 'string'}, 'children': {'type': 'array', 'items': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'industry_name': {'type': 'string'}}}}}}}}}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
    ('follow', 'POST'): {400: {'headers': None, 'schema': {'type': 'object', 'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message']}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 204: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
    ('follow', 'DELETE'): {400: {'headers': None, 'schema': {'type': 'object', 'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message']}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 204: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
    ('article_id_invalid', 'PUT'): {400: {'headers': None, 'schema': {'type': 'object', 'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message']}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 204: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
    ('account_login', 'POST'): {400: {'headers': None, 'schema': {'type': 'object', 'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message']}}, 401: {'headers': None, 'schema': None}, 204: {'headers': None, 'schema': None}},
    ('newfollow', 'POST'): {400: {'headers': None, 'schema': {'type': 'object', 'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message']}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 204: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
    ('articles', 'GET'): {200: {'headers': None, 'schema': {'type': 'object', 'properties': {'count': {'type': 'integer'}, 'articles': {'type': 'array', 'items': {'type': 'object', 'properties': {'time': {'type': 'string'}, 'id': {'type': 'integer'}, 'is_read': {'type': 'integer'}, 'follow_name': {'type': 'string'}, 'title': {'type': 'string'}, "follow_type'": {'type': 'integer', 'enum': [1, 2]}}}}}}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
    ('follow_state', 'GET'): {200: {'headers': None, 'schema': {'type': 'object', 'properties': {'industry': {'type': 'integer'}, 'company': {'type': 'integer'}}}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}},
    ('follows', 'GET'): {200: {'headers': None, 'schema': {'type': 'object', 'properties': {'industry': {'type': 'array', 'items': {'type': 'object', 'properties': {'id': {'type': 'integer'}, 'industry_name': {'type': 'string'}, 'children_count': {'type': 'integer'}}}}, 'company': {'type': 'array', 'items': {'type': 'object', 'properties': {'short_name': {'type': 'integer'}, 'id': {'type': 'integer'}, 'company_name': {'type': 'string'}}}}}}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
}

scopes = {
    ('home', 'GET'): [],
    ('article_id', 'GET'): [],
    ('search', 'GET'): [],
    ('follow', 'POST'): [],
    ('follow', 'DELETE'): [],
    ('article_id_invalid', 'PUT'): [],
    ('account_login', 'POST'): [],
    ('newfollow', 'POST'): [],
    ('articles', 'GET'): [],
    ('follow_state', 'GET'): [],
    ('follows', 'GET'): [],
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
