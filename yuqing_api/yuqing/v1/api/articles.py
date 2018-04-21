# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from sqlalchemy import and_
from datetime import datetime, timedelta
from core.PackageDB import industry_article,employee_article,company_article,article,follow_company,company,_connectDBdata_

class Articles(ApiHandler):

    def get(self):
        user = self.get_current_user()
        if not user.valid:
            return None ,401,None
        if user.employee.id is None:
            return None ,403,None
        page_index = self.args['page_index']
        follow_type = self.args['follow_type']
        page_size = 20
        dbsession = _connectDBdata_()
        #文章信息获取
        respone = {}
        articleinfoarray = []
        for row in dbsession.query(article.id, article.title, company.company_name, article.publish_time, employee_article.is_read)\
            .join(company_article, article.id == company_article.article_id)\
            .join(follow_company, follow_company.company_id == company_article.company_id)\
            .join(company, company.id == company_article.company_id)\
            .join(employee_article, employee_article.article_id == article.id)\
            .filter(and_(follow_company.is_follow == follow_type, employee_article.is_invalid == 0,follow_company.employee_id == user.employee.id,employee_article.employee_id==user.employee.id))\
            .order_by(article.publish_time.desc()).slice((page_index - 1) * page_size, page_index * page_size):
            articleinfodic = {}
            articleinfodic['id'] = row[0]
            articleinfodic['title'] = row[1]
            articleinfodic['follow_name'] = row[2]
            articleinfodic['follow_type'] = follow_type
            articleinfodic['is_read'] = row[4]
            articleinfodic['time'] = row[3].strftime('%Y-%m-%d %H:%M:%S')
            articleinfoarray.append(articleinfodic)
        respone['articles'] = articleinfoarray
        dbsession.close()
        return respone, 200, None