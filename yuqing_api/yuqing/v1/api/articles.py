# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from sqlalchemy import and_
from datetime import datetime, timedelta
from core.PackageDB import industry_article,employee_article,company_article,article,_connectDBdata_

class Articles(ApiHandler):

    def get(self):
        page_index = self.args['page_index']
        follow_type = self.args['follow_type']
        page_size = 20
        user = self.get_current_user()
        if user.valid:
            dbsession = _connectDBdata_()
            #文章信息获取
            respone = {}
            articleinfoarray = []
            for row in dbsession.query(article.id,article.title,employee_article.is_read,employee_article.send_time)\
                .join(employee_article,article.id == employee_article.article_id)\
                .filter(and_(employee_article.employee_id == user.employee.id,employee_article.is_send==0,employee_article.is_invalid==0)).order_by(employee_article.send_time.desc()).slice((page_index - 1) * page_size, page_index * page_size):
                articleinfodic = {}
                articleinfodic['id'] = row[0]
                articleinfodic['title'] = row[1]
                articleinfodic['follow_type'] = 1
                articleinfodic['is_read'] = row[2]
                articleinfodic['time'] = row[3].strftime('%Y-%m-%d %H:%M:%S')
                articleinfoarray.append(articleinfodic)
            respone['articles'] = articleinfoarray
            return respone, 200, None