# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from datetime import datetime, timedelta

from sqlalchemy import and_

from core.PackageDB import (_connectDBdata_, article, company, company_article,
                            employee_article, follow_company, follow_industry,
                            industry, industry_article)

from . import ApiHandler
from .. import schemas


class Articles(ApiHandler):
    def get(self):
        user = self.get_current_user()
        if not user.valid:
            return None, 401, None
        if user.session.employee_id is None:
            return None, 403, None
        page_index = self.args['page_index']
        follow_type = self.args['follow_type']
        key = ''
        if 'key' in self.args:
            key = self.args['key'].strip()  #TODO 特殊字符过滤

        page_size = 20
        skip = (page_index - 1) * page_size
        take = page_index * page_size
       
        respone = {}
        articles = []

        # 文章信息获取
        dbsession = _connectDBdata_()
        if follow_type == 1:
            articles = dbsession.query(article.id, article.title, company.company_name, article.publish_time, employee_article.is_read)\
                .join(company_article, article.id == company_article.article_id)\
                .join(follow_company, follow_company.company_id == company_article.company_id)\
                .join(company, company.id == company_article.company_id)\
                .join(employee_article, employee_article.article_id == article.id)\
                .filter(and_(follow_company.is_follow == 1, employee_article.is_invalid == 0, follow_company.employee_id == user.employee.id, employee_article.employee_id == user.employee.id))
            if len(key):
                articles = articles.filter(company.company_name == key)

            # 计算数量
            respone['count'] = articles.count()
            articles = articles.order_by(article.publish_time.desc(),article.id.desc()).slice(
                skip, take)
        else:
            articles = dbsession.query(article.id, article.title, industry.industry_name, article.publish_time, employee_article.is_read)\
                .join(industry_article, article.id == industry_article.article_id)\
                .join(follow_industry, follow_industry.industry_id == industry_article.industry_id)\
                .join(industry, industry.id == industry_article.industry_id)\
                .join(employee_article, employee_article.article_id == article.id)\
                .filter(and_(follow_industry.is_follow == 1, employee_article.is_invalid == 0, follow_industry.employee_id == user.employee.id, employee_article.employee_id == user.employee.id))
            if len(key):
                articles = articles.filter(industry.industry_name == key)

            # 计算数量
            respone['count'] = articles.count()
            articles = articles.order_by(article.publish_time.desc(),article.id.desc()).slice(
                skip, take)
        dbsession.close()

        articleinfoarray = []
        for row in articles:
            articleinfodic = {}
            articleinfodic['id'] = row[0]
            articleinfodic['title'] = row[1]
            articleinfodic['follow_name'] = row[2]
            articleinfodic['follow_type'] = follow_type
            articleinfodic['is_read'] = row[4]
            articleinfodic['time'] = row[3].strftime('%Y/%m/%d %H:%M:%S')
            articleinfoarray.append(articleinfodic)
        respone['articles'] = articleinfoarray
        return respone, 200, None
