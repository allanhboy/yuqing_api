# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import json
import urllib.parse
import urllib.request
from datetime import datetime, timedelta

from sqlalchemy import exists

from core.PackageDB import (_connectDBdata_, article, company, company_article,
                            employee_article, employee_follow, follow_company,
                            industry_article)
from core.webconfig import spiderurl

from . import ApiHandler
from .. import schemas

class Newfollow(ApiHandler):

    def post(self):
        user = self.get_current_user()
        if not user.valid:
            return None, 401, None
        if user.session.employee_id is None:
            return None, 403, None

        company_name = self.json['company_name']
        if company_name is None or len(company_name) <= 0:
            return None, 400, None
        short_name = self.json['short_name']
        if short_name is None or len(short_name) <= 0:
            return None, 400, None
        datenow = datetime.now()
        dbsession = _connectDBdata_()
        try:
            dbcompanyinfo = dbsession.query(company).filter(
                company.company_name == company_name).one_or_none()
            # 添加新的公司
            if dbcompanyinfo is None:
                dbcompanyinfo = company(
                    company_name=company_name, short_name=short_name, is_chinaipo=0, url='')
                dbsession.add(dbcompanyinfo)
                dbsession.flush()

                dbfollowcompany = follow_company(
                    employee_id=user.employee.id, company_id=dbcompanyinfo.id)
                dbsession.add(dbfollowcompany)
            else:
                dbfollowcompany = dbsession.query(follow_company).filter(
                    follow_company.company_id == dbcompanyinfo.id, follow_company.employee_id == user.employee.id).one_or_none()
                if dbfollowcompany:
                    # 公司已经存在，且已取消关注数据
                    if dbfollowcompany.is_follow == 0:
                        dbfollowcompany.is_follow = 1
                        dbfollowcompany.follow_time = datetime.now()
                    #公司存在，并且已经关注
                    else:
                        return None, 204, None
                else:
                    # 公司已经存在，无关注数据
                    dbfollowcompany = follow_company(
                        employee_id=user.employee.id, company_id=dbcompanyinfo.id)
                    dbsession.add(dbfollowcompany)
            dbsession.query(employee_follow).filter(
                employee_follow.id == user.employee.id).update({'company_count': employee_follow.company_count+1})

            # 公司和文章关联
            dbarticleinfo = dbsession.query(article.id).filter(~exists().where(
                company_article.article_id == article.id).where(
                company_article.company_id == dbcompanyinfo.id)).filter(article.text.like('%'+short_name+'%')).all()
            companyarticle = []
            for row in dbarticleinfo:
                dbcompanyarticleinfo = company_article(
                    company_id=dbcompanyinfo.id, article_id=row[0])
                companyarticle.append(dbcompanyarticleinfo)
            dbsession.add_all(companyarticle)
            dbsession.flush()

            # 操作员工关注文章
            faker_employee_article = []
            for row in dbsession.query(company_article.article_id, article.publish_time)\
                .join(article, article.id == company_article.article_id)\
                .filter(company_article.company_id == dbcompanyinfo.id)\
                    .filter(~exists().where(employee_article.article_id == company_article.article_id).where(employee_article.employee_id == user.employee.id)).all():
                dbemployeearticleinfo = employee_article(
                    employee_id=user.employee.id, article_id=row[0], is_read=0, is_invalid=0, is_send=1, send_time=datetime.now())
                if row[1].strftime('%Y/%m/%d') < datenow.strftime('%Y/%m/%d'):
                    dbemployeearticleinfo.is_read = 1
                faker_employee_article.append(dbemployeearticleinfo)
            dbsession.add_all(faker_employee_article)
            dbsession.commit()
            dbsession.close()
            # 爬取文
            try:
                key_code = urllib.request.quote(short_name)  # 因为URL里含中文，需要进行编码
                url_all = spiderurl+key_code
                req = urllib.request.Request(url_all)
                response = urllib.request.urlopen(req)
                the_page = response.read()
            except:
                print('爬取失败')
            return None, 204, None
        except:
            return None, 400, None
        finally:
            dbsession.close()
