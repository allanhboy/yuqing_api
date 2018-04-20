# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


from core.PackageDB import article,_connectDBdata_

class ArticleId(ApiHandler):

    def get(self, id):
        user = self.get_current_user()
        if user.valid:
            dbsession = _connectDBdata_()
            #文章详情信息获取
            dbarticleinfo = dbsession.query(article).filter(article.id == id).one()
            reponse = {}
            reponse['id'] = dbarticleinfo.id
            reponse['title'] = dbarticleinfo.title
            reponse['source'] = dbarticleinfo.source_site
            reponse['source_url'] = dbarticleinfo.url
            reponse['content'] = dbarticleinfo.text
            dbsession.close()
            return reponse, 200, None
