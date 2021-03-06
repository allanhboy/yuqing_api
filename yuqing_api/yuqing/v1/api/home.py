# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import json

from sqlalchemy import and_

from core.PackageDB import (_connectDBdata_, article, company, company_article,
                            employee, employee_article, follow_company,
                            follow_industry, industry_article)
from core.webconfig import alicdnserver

from . import ApiHandler
from .. import schemas

class Home(ApiHandler):
    def get(self):
        user = self.get_current_user()
        if not user.valid:
            return None, 401, None
        if user.session.employee_id is None:
            return None, 403, None
        respone = {}
        dbsession = _connectDBdata_()

        # 获取用户信息
        dbemployee = dbsession.query(employee.realname, employee.picture).filter(
            employee.id == user.employee.id).one()
        var_employ = {}
        var_employ['realname'] = dbemployee[0]
        var_employ['picture'] = alicdnserver+dbemployee[1]
        respone['employee'] = var_employ

        # 新增公司舆情数
        respone['new_company_news'] = dbsession.query(article.id)\
            .join(company_article, article.id == company_article.article_id)\
            .join(follow_company, follow_company.company_id == company_article.company_id)\
            .join(employee_article, employee_article.article_id == article.id)\
            .filter(and_(follow_company.is_follow == 1, employee_article.is_invalid == 0, follow_company.employee_id == user.employee.id, employee_article.employee_id == user.employee.id, employee_article.is_read == 0))\
            .count()

        # 新增行业舆情数
        respone['new_industry_news'] = dbsession.query(article.id)\
            .join(industry_article, article.id == industry_article.article_id)\
            .join(follow_industry, follow_industry.industry_id == industry_article.industry_id)\
            .join(employee_article, employee_article.article_id == article.id)\
            .filter(and_(follow_industry.is_follow == 1, employee_article.is_invalid == 0, follow_industry.employee_id == user.employee.id, employee_article.employee_id == user.employee.id, employee_article.is_read == 0))\
            .count()

        # 公司第一页舆情列表
        var_articles = []
        db = dbsession.query(article.id, article.title, company.company_name, article.publish_time, employee_article.is_read)\
            .join(company_article, article.id == company_article.article_id)\
            .join(follow_company, follow_company.company_id == company_article.company_id)\
            .join(company, company.id == company_article.company_id)\
            .join(employee_article, employee_article.article_id == article.id)\
            .filter(and_(follow_company.is_follow == 1, employee_article.is_invalid == 0, follow_company.employee_id == user.employee.id, employee_article.employee_id == user.employee.id))\
            .order_by(article.publish_time.desc(),article.id.desc()).limit(20)
        dbsession.close()
        for row in db:
            var_article = {}
            var_article['id'] = row[0]
            var_article['title'] = row[1]
            var_article['follow_type'] = 1
            var_article['follow_name'] = row[2]
            var_article['time'] = row[3].strftime('%Y/%m/%d %H:%M:%S')
            var_article['is_read'] = row[4]
            var_articles.append(var_article)
        respone['articles'] = var_articles
        return respone, 200, None
