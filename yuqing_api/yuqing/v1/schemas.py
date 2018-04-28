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


DefinitionsError = {'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message'], 'type': 'object'}

validators = {
    ('search', 'GET'): {'args': {'properties': {'follow_type': {'enum': [1, 2], 'type': 'integer'}, 'key': {'type': 'string'}, 'type': {'type': 'integer'}}, 'required': []}},
    ('articles', 'GET'): {'args': {'properties': {'follow_type': {'type': 'integer'}, 'key': {'type': 'string'}, 'page_index': {'type': 'integer'}}, 'required': []}},
    ('account_login', 'POST'): {'json': {'properties': {'username': {'type': 'string'}, 'password': {'type': 'string'}}, 'type': 'object'}},
    ('wechat_login', 'POST'): {'json': {'properties': {'code': {'description': '调用接口wx.login() 获取临时登录凭证（code）', 'type': 'string'}, 'random': {'description': '小程序客户端随机生成6位数字', 'type': 'string'}}, 'type': 'object'}},
    ('newfollow', 'POST'): {'json': {'properties': {'company_name': {'type': 'string'}, 'short_name': {'type': 'string'}}, 'type': 'object'}},
    ('follow', 'POST'): {'json': {'properties': {'follow_type': {'type': 'integer', 'enum': [1, 2]}, 'id': {'type': 'integer'}}, 'type': 'object'}},
    ('follow', 'DELETE'): {'json': {'properties': {'follow_type': {'type': 'integer', 'enum': [1, 2]}, 'id': {'type': 'integer'}}, 'type': 'object'}},
}

filters = {
    ('home', 'GET'): {200: {'schema': {'properties': {'new_industry_news': {'type': 'integer'}, 'new_company_news': {'type': 'integer'}, 'employee': {'properties': {'picture': {'type': 'string'}, 'realname': {'type': 'string'}}, 'type': 'object'}, 'articles': {'items': {'properties': {'id': {'type': 'integer'}, 'time': {'type': 'string'}, 'title': {'type': 'string'}, 'is_read': {'type': 'integer'}, 'follow_name': {'type': 'string'}, 'follow_type': {'type': 'integer', 'enum': [1, 2]}}, 'type': 'object'}, 'type': 'array'}}, 'type': 'object'}, 'headers': None}, 401: {'schema': None, 'headers': None}, 403: {'schema': None, 'headers': None}, 500: {'schema': None, 'headers': None}},
    ('follow_state', 'GET'): {200: {'schema': {'properties': {'industry': {'type': 'integer'}, 'company': {'type': 'integer'}}, 'type': 'object'}, 'headers': None}, 401: {'schema': None, 'headers': None}, 403: {'schema': None, 'headers': None}},
    ('search', 'GET'): {200: {'schema': {'properties': {'follows': {'items': {'properties': {'id': {'type': 'integer'}, 'children_count': {'type': 'integer'}, 'children': {'items': {'properties': {'id': {'type': 'string'}, 'industry_name': {'type': 'string'}}, 'type': 'object'}, 'type': 'array'}, 'company_name': {'type': 'string'}, 'follow_type': {'type': 'integer', 'enum': [1, 2]}, 'industry_name': {'type': 'string'}, 'short_name': {'type': 'string'}}, 'type': 'object'}, 'type': 'array'}}, 'type': 'object'}, 'headers': None}, 401: {'schema': None, 'headers': None}, 403: {'schema': None, 'headers': None}, 500: {'schema': None, 'headers': None}},
    ('articles', 'GET'): {200: {'schema': {'properties': {'articles': {'items': {'properties': {'id': {'type': 'integer'}, 'time': {'type': 'string'}, 'title': {'type': 'string'}, 'is_read': {'type': 'integer'}, "follow_type'": {'type': 'integer', 'enum': [1, 2]}, 'follow_name': {'type': 'string'}}, 'type': 'object'}, 'type': 'array'}, 'count': {'type': 'integer'}}, 'type': 'object'}, 'headers': None}, 401: {'schema': None, 'headers': None}, 403: {'schema': None, 'headers': None}, 500: {'schema': None, 'headers': None}},
    ('account_login', 'POST'): {400: {'schema': {'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message'], 'type': 'object'}, 'headers': None}, 401: {'schema': None, 'headers': None}, 204: {'schema': None, 'headers': None}},
    ('article_id_invalid', 'PUT'): {400: {'schema': {'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message'], 'type': 'object'}, 'headers': None}, 401: {'schema': None, 'headers': None}, 403: {'schema': None, 'headers': None}, 500: {'schema': None, 'headers': None}, 204: {'schema': None, 'headers': None}},
    ('wechat_login', 'POST'): {200: {'schema': {'properties': {'session': {'description': '小程序登录凭证,对应表session.id', 'type': 'string'}, 'expire_time': {'description': '对应表session.expire_time', 'type': 'string'}, 'is_binding': {'description': 'openid在表employee找不到返回False,否则为True', 'type': 'boolean'}}, 'type': 'object'}, 'headers': None}, 400: {'schema': {'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message'], 'type': 'object'}, 'headers': None}},
    ('article_id', 'GET'): {200: {'schema': {'properties': {'id': {'type': 'integer'}, 'source': {'type': 'string'}, 'title': {'type': 'string'}, "follow_type'": {'type': 'integer'}, 'content': {'type': 'string'}, 'follow_name': {'type': 'string'}, 'source_url': {'type': 'string'}}, 'type': 'object'}, 'headers': None}, 401: {'schema': None, 'headers': None}, 404: {'schema': None, 'headers': None}, 403: {'schema': None, 'headers': None}, 500: {'schema': None, 'headers': None}},
    ('newfollow', 'POST'): {400: {'schema': {'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message'], 'type': 'object'}, 'headers': None}, 401: {'schema': None, 'headers': None}, 403: {'schema': None, 'headers': None}, 500: {'schema': None, 'headers': None}, 204: {'schema': None, 'headers': None}},
    ('follow', 'POST'): {400: {'schema': {'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message'], 'type': 'object'}, 'headers': None}, 401: {'schema': None, 'headers': None}, 403: {'schema': None, 'headers': None}, 500: {'schema': None, 'headers': None}, 204: {'schema': None, 'headers': None}},
    ('follow', 'DELETE'): {400: {'schema': {'properties': {'code': {'type': 'integer'}, 'message': {'type': 'string'}}, 'required': ['code', 'message'], 'type': 'object'}, 'headers': None}, 401: {'schema': None, 'headers': None}, 403: {'schema': None, 'headers': None}, 500: {'schema': None, 'headers': None}, 204: {'schema': None, 'headers': None}},
    ('follows', 'GET'): {200: {'schema': {'properties': {'industry': {'items': {'properties': {'children_industry': {'items': {'properties': {'children_industry': {'items': {'properties': {'id': {'type': 'integer'}, 'children_count': {'type': 'integer'}, 'industry_name': {'type': 'string'}}, 'type': 'object'}, 'type': 'array'}, 'id': {'type': 'integer'}, 'children_count': {'type': 'integer'}, 'industry_name': {'type': 'string'}}, 'type': 'object'}, 'type': 'array'}, 'id': {'type': 'integer'}, 'children_count': {'type': 'integer'}, 'industry_name': {'type': 'string'}}, 'type': 'object'}, 'type': 'array'}, 'company': {'items': {'properties': {'company_name': {'type': 'string'}, 'id': {'type': 'integer'}, 'short_name': {'type': 'integer'}}, 'type': 'object'}, 'type': 'array'}}, 'type': 'object'}, 'headers': None}, 401: {'schema': None, 'headers': None}, 403: {'schema': None, 'headers': None}, 500: {'schema': None, 'headers': None}},
}

scopes = {
    ('home', 'GET'): [],
    ('follow_state', 'GET'): [],
    ('search', 'GET'): [],
    ('articles', 'GET'): [],
    ('account_login', 'POST'): [],
    ('article_id_invalid', 'PUT'): [],
    ('article_id', 'GET'): [],
    ('newfollow', 'POST'): [],
    ('follow', 'POST'): [],
    ('follow', 'DELETE'): [],
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
