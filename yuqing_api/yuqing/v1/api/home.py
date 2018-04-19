# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from sqlalchemy import and_
from core.PackageDB import employee, article, company, employee_article, company_article,follow_company, industry_article, _connectDBdata_
import json


class Home(ApiHandler):


    def get(self):
        user = self.get_current_user()
        respone = {}
        if user.valid:
            dbsession = _connectDBdata_()

            # 获取用户信息
            dbemployee = dbsession.query(employee.realname, employee.picture).filter(
                employee.id == user.employee.id).one()
            var_employ = {}
            var_employ['realname'] = dbemployee[0]
            var_employ['picture'] = dbemployee[1]
            respone['employee'] = var_employ

            respone['new_company_news'] = dbsession.query(employee_article.article_id).filter(and_(employee_article.employee_id == user.employee.id, employee_article.is_send == 1, employee_article.is_read == 0)).filter(exists().where(
                company_article.article_id == employee_article.article_id)).distinct().count()

            respone['new_industry_news'] = dbsession.query(employee_article.article_id).filter(and_(employee_article.employee_id == user.employee.id, employee_article.is_send == 1, employee_article.is_read == 0)).filter(exists().where(
                industry_article.article_id == employee_article.article_id)).group_by().distinct().count()

            var_articles = []
            for row in dbsession.query(article.id, article.title, company.short_name, article.publish_time, employee_article.is_read).join(employee_article, article.id == employee_article.article_id).join(company, follow_company.company_id == company.id).join(follow_company, follow_company.employee_id == employee_article.employee_id).filter(and_(follow_company.employee_id == user.employee.id), follow_company.is_follow == 1).all():
                var_article = {}
                var_article['id'] = row[0]
                var_article['title'] = row[1]
                var_article['follow_type'] = 1
                var_article['follow_name'] = row[2]
                var_article['time'] = row[3]
                var_article['is_read'] = row[4]
                var_articles.append(var_article)
            respone['articles'] = var_articles

        return respone, 200, None
