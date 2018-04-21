# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from sqlalchemy import and_
from core.PackageDB import employee, article, company, employee_article, company_article, follow_company, industry_article, _connectDBdata_
import json


class Home(ApiHandler):

    def get(self):
        user = self.get_current_user()
        if not user.valid:
            return None ,401,None
        if user.employee.id is None:
            return None ,403,None
        respone = {}
        dbsession = _connectDBdata_()

        # 获取用户信息
        dbemployee = dbsession.query(employee.realname, employee.picture).filter(
            employee.id == user.employee.id).one()
        var_employ = {}
        var_employ['realname'] = dbemployee[0]
        var_employ['picture'] = dbemployee[1]
        respone['employee'] = var_employ

        # 新增公司舆情数
        respone['new_company_news'] = dbsession.query(employee_article.article_id).filter(and_(employee_article.employee_id == user.employee.id, employee_article.is_send == 1, employee_article.is_read == 0)).join(
            company_article, company_article.article_id == employee_article.article_id).distinct().count()

        # 新增行业舆情数
        respone['new_industry_news'] = dbsession.query(employee_article.article_id).filter(and_(employee_article.employee_id == user.employee.id, employee_article.is_send == 1, employee_article.is_read == 0)).join(
            industry_article, industry_article.article_id == employee_article.article_id).distinct().count()

        # 公司第一页舆情列表
        var_articles = []
        for row in dbsession.query(article.id, article.title, company.short_name, article.publish_time, employee_article.is_read).join(employee_article, article.id == employee_article.article_id).join(follow_company, follow_company.employee_id == employee_article.employee_id).join(company, follow_company.company_id == company.id).filter(and_(follow_company.employee_id == user.employee.id), follow_company.is_follow == 1).order_by(employee_article.send_time.desc()).limit(20):
            var_article = {}
            var_article['id'] = row[0]
            var_article['title'] = row[1]
            var_article['follow_type'] = 1
            var_article['follow_name'] = row[2]
            var_article['time'] = row[3].strftime('%Y-%m-%d %H:%M:%S')
            var_article['is_read'] = row[4]
            var_articles.append(var_article)
        respone['articles'] = var_articles
        dbsession.close()
        return respone, 200, None
