# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.wechat_login import WechatLogin
from .api.account_login import AccountLogin


url_prefix = 'v1'

routes = [
    dict(resource=WechatLogin, urls=[r"/wechat/login"], endpoint='wechat_login'),
    dict(resource=AccountLogin, urls=[r"/account/login"], endpoint='account_login'),
]

def load_uris(config):
    try:
        config.update_uri(routes, url_prefix)
    except:
        pass