# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.article_id import ArticleId
from .api.follows import Follows
from .api.article_id_invalid import ArticleIdInvalid
from .api.articles import Articles
from .api.follow import Follow
from .api.search import Search
from .api.home import Home
from .api.account_login import AccountLogin
from .api.wechat_login import WechatLogin
from .api.newfollow import Newfollow


url_prefix = 'v1'

routes = [
    dict(resource=ArticleId, urls=[r"/article/(?P<id>[^/]+?)"], endpoint='article_id'),
    dict(resource=Follows, urls=[r"/follows"], endpoint='follows'),
    dict(resource=ArticleIdInvalid, urls=[r"/article/(?P<id>[^/]+?)/invalid"], endpoint='article_id_invalid'),
    dict(resource=Articles, urls=[r"/articles"], endpoint='articles'),
    dict(resource=Follow, urls=[r"/follow"], endpoint='follow'),
    dict(resource=Search, urls=[r"/search"], endpoint='search'),
    dict(resource=Home, urls=[r"/home"], endpoint='home'),
    dict(resource=AccountLogin, urls=[r"/account/login"], endpoint='account_login'),
    dict(resource=WechatLogin, urls=[r"/wechat/login"], endpoint='wechat_login'),
    dict(resource=Newfollow, urls=[r"/newfollow"], endpoint='newfollow'),
]

def load_uris(config):
    try:
        config.update_uri(routes, url_prefix)
    except:
        pass