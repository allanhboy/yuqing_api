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


DefinitionsError = {'required': ['code', 'message'], 'properties': {'message': {'type': 'string'}, 'code': {'type': 'integer'}}, 'type': 'object'}

validators = {
    ('wechat_login', 'POST'): {'json': {'properties': {'random': {'description': '小程序客户端随机生成6位数字', 'type': 'string'}, 'code': {'description': '调用接口wx.login() 获取临时登录凭证（code）', 'type': 'string'}}, 'type': 'object'}},
    ('account_login', 'POST'): {'json': {'properties': {'password': {'type': 'string'}, 'username': {'type': 'string'}}, 'type': 'object'}},
    ('newfollow', 'POST'): {'json': {'properties': {'short_name': {'type': 'string'}, 'company_name': {'type': 'string'}}, 'type': 'object'}},
    ('follow', 'DELETE'): {'json': {'properties': {'follow_type': {'enum': [1, 2], 'type': 'integer'}, 'id': {'type': 'integer'}}, 'type': 'object'}},
    ('follow', 'POST'): {'json': {'properties': {'follow_type': {'enum': [1, 2], 'type': 'integer'}, 'id': {'type': 'integer'}}, 'type': 'object'}},
    ('articles', 'GET'): {'args': {'required': [], 'properties': {'key': {'type': 'string'}, 'page_index': {'type': 'integer'}, 'follow_type': {'type': 'integer'}}}},
    ('search', 'GET'): {'args': {'required': [], 'properties': {'follow_type': {'enum': [1, 2], 'type': 'integer'}, 'key': {'type': 'string'}}}},
}

filters = {
    ('wechat_login', 'POST'): {200: {'headers': None, 'schema': {'properties': {'expire_time': {'description': '对应表session.expire_time', 'type': 'string'}, 'session': {'description': '小程序登录凭证,对应表session.id', 'type': 'string'}, 'is_binding': {'description': 'openid在表employee找不到返回False,否则为True', 'type': 'boolean'}}, 'type': 'object'}}, 400: {'headers': None, 'schema': {'required': ['code', 'message'], 'properties': {'message': {'type': 'string'}, 'code': {'type': 'integer'}}, 'type': 'object'}}},
    ('article_id', 'GET'): {200: {'headers': None, 'schema': {'properties': {'id': {'type': 'integer'}, 'source': {'type': 'string'}, 'title': {'type': 'string'}, 'source_url': {'type': 'string'}, "follow_type'": {'type': 'integer'}, 'follow_name': {'type': 'string'}, 'content': {'type': 'string'}}, 'type': 'object'}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
    ('account_login', 'POST'): {400: {'headers': None, 'schema': {'required': ['code', 'message'], 'properties': {'message': {'type': 'string'}, 'code': {'type': 'integer'}}, 'type': 'object'}}, 401: {'headers': None, 'schema': None}, 204: {'headers': None, 'schema': None}},
    ('home', 'GET'): {200: {'headers': None, 'schema': {'properties': {'employee': {'properties': {'picture': {'type': 'string'}, 'realname': {'type': 'string'}}, 'type': 'object'}, 'new_company_news': {'type': 'integer'}, 'new_industry_news': {'type': 'integer'}, 'articles': {'items': {'properties': {'title': {'type': 'string'}, 'is_read': {'type': 'integer'}, 'time': {'type': 'string'}, 'follow_type': {'enum': [1, 2], 'type': 'integer'}, 'follow_name': {'type': 'string'}, 'id': {'type': 'integer'}}, 'type': 'object'}, 'type': 'array'}}, 'type': 'object'}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
    ('article_id_invalid', 'PUT'): {400: {'headers': None, 'schema': {'required': ['code', 'message'], 'properties': {'message': {'type': 'string'}, 'code': {'type': 'integer'}}, 'type': 'object'}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}, 204: {'headers': None, 'schema': None}},
    ('newfollow', 'POST'): {400: {'headers': None, 'schema': {'required': ['code', 'message'], 'properties': {'message': {'type': 'string'}, 'code': {'type': 'integer'}}, 'type': 'object'}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}, 204: {'headers': None, 'schema': None}},
    ('follow', 'DELETE'): {400: {'headers': None, 'schema': {'required': ['code', 'message'], 'properties': {'message': {'type': 'string'}, 'code': {'type': 'integer'}}, 'type': 'object'}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}, 204: {'headers': None, 'schema': None}},
    ('follow', 'POST'): {400: {'headers': None, 'schema': {'required': ['code', 'message'], 'properties': {'message': {'type': 'string'}, 'code': {'type': 'integer'}}, 'type': 'object'}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}, 204: {'headers': None, 'schema': None}},
    ('articles', 'GET'): {200: {'headers': None, 'schema': {'properties': {'articles': {'items': {'properties': {'title': {'type': 'string'}, 'is_read': {'type': 'integer'}, 'time': {'type': 'string'}, "follow_type'": {'enum': [1, 2], 'type': 'integer'}, 'follow_name': {'type': 'string'}, 'id': {'type': 'integer'}}, 'type': 'object'}, 'type': 'array'}}, 'type': 'object'}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
    ('follows', 'GET'): {200: {'headers': None, 'schema': {'properties': {'company': {'items': {'properties': {'short_name': {'type': 'integer'}, 'company_name': {'type': 'string'}, 'id': {'type': 'integer'}}, 'type': 'object'}, 'type': 'array'}, 'industry': {'items': {'properties': {'industry_name': {'type': 'string'}, 'children_count': {'type': 'integer'}, 'id': {'type': 'integer'}}, 'type': 'object'}, 'type': 'array'}}, 'type': 'object'}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
    ('follow_state', 'GET'): {200: {'headers': None, 'schema': {'properties': {'company': {'type': 'integer'}, 'industry': {'type': 'integer'}}, 'type': 'object'}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}},
    ('search', 'GET'): {200: {'headers': None, 'schema': {'properties': {'follows': {'items': {'properties': {'short_name': {'type': 'string'}, 'children_count': {'type': 'integer'}, 'industry_name': {'type': 'string'}, 'follow_type': {'enum': [1, 2], 'type': 'integer'}, 'company_name': {'type': 'string'}, 'children': {'items': {'properties': {'industry_name': {'type': 'string'}, 'id': {'type': 'string'}}, 'type': 'object'}, 'type': 'array'}, 'id': {'type': 'integer'}}, 'type': 'object'}, 'type': 'array'}}, 'type': 'object'}}, 401: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 500: {'headers': None, 'schema': None}},
}

scopes = {
    ('article_id', 'GET'): [],
    ('account_login', 'POST'): [],
    ('home', 'GET'): [],
    ('article_id_invalid', 'PUT'): [],
    ('newfollow', 'POST'): [],
    ('follow', 'DELETE'): [],
    ('follow', 'POST'): [],
    ('articles', 'GET'): [],
    ('follows', 'GET'): [],
    ('follow_state', 'GET'): [],
    ('search', 'GET'): [],
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
