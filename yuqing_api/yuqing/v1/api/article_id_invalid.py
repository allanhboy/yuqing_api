# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from sqlalchemy import and_

from core.PackageDB import _connectDBdata_, employee_article

from . import ApiHandler
from .. import schemas


class ArticleIdInvalid(ApiHandler):
    def put(self, id):
        user = self.get_current_user()
        if not user.valid:
            return None, 401, None
        if user.session.employee_id is None:
            return None, 403, None

        dbsession = _connectDBdata_()
        try:
            dbsession.query(employee_article).filter(
                and_(employee_article.employee_id == user.employee.id,
                     employee_article.article_id == id,
                     employee_article.is_invalid == 0)).update({
                         'is_invalid': 1
                     })
            dbsession.commit()
            return None, 204, None
        except:
            return None, 400, None
        finally:
            dbsession.close()
