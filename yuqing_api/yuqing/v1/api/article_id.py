# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


from core.PackageDB import article, employee_article, _connectDBdata_
from sqlalchemy import and_


class ArticleId(ApiHandler):

    def get(self, id):
        user = self.get_current_user()
        if not user.valid:
            return None, 401, None
        if user.session.employee_id is None:
            return None, 403, None

        # 文章详情信息获取
        dbsession = _connectDBdata_()
        dbarticleinfo = dbsession.query(article, employee_article.is_invalid)\
            .join(employee_article, and_(employee_article.article_id == article.id, employee_article.employee_id == user.employee.id))\
            .filter(article.id == id, employee_article.is_invalid == 0).one_or_none()
        if dbarticleinfo is None:
            return None, 404, None

        dbsession.query(employee_article)\
            .filter(and_(employee_article.article_id == id, employee_article.employee_id == user.employee.id, employee_article.is_read == 0))\
            .update({'is_read': 1})

        reponse = {}
        reponse['id'] = dbarticleinfo[0].id
        reponse['title'] = dbarticleinfo[0].title
        reponse['source'] = dbarticleinfo[0].source_site
        reponse['source_url'] = dbarticleinfo[0].url
        reponse['content'] = dbarticleinfo[0].text
        reponse['time'] = dbarticleinfo[0].publish_time.strftime(
            '%Y/%m/%d %H:%M:%S')

        dbsession.commit()
        dbsession.close()
        return reponse, 200, None
