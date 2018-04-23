# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from core.PackageDB import employee_article,_connectDBdata_
from sqlalchemy import and_

class ArticleIdInvalid(ApiHandler):

    def put(self, id):
        user = self.get_current_user()
        if not user.valid:
            return None ,401,None
        if user.employee.id is None:
            return None ,403,None
        
        dbsession =_connectDBdata_()
        dbemployeearticleinfo = dbsession.query(employee_article).filter(and_(employee_article.employee_id == user.employee.id,employee_article.article_id == id)).one_or_none()
        if dbemployeearticleinfo:
            dbemployeearticleinfo.is_invalid = 1
            dbsession.add(dbemployeearticleinfo)
            dbsession.commit()
            dbsession.close()
            return None, 204, None
        else:
            dbsession.close()
            return {"message": "未找到该文章","code": 0},400,None