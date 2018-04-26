# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

import urllib.request
from datetime import datetime, timedelta
import json

from core.PackageDB import company,employee_follow,follow_company,company_article,employee_article,article,_connectDBdata_

class Newfollow(ApiHandler):

    def post(self):
        user = self.get_current_user()
        if not user.valid:
            return None ,401,None
        if user.session.employee_id is None:
            return None ,403,None
            
        company_name = self.json['company_name']
        short_name = self.json['short_name']

        dbsession =_connectDBdata_()


        dbcompanyinfo = dbsession.query(company).filter(company.company_name == company_name).one_or_none()
        #添加新的公司
        if dbcompanyinfo is None:
            dbcompanyinfo = company(company_name = company_name,short_name = short_name,is_chinaipo = 0,url = '')
            dbsession.add(dbcompanyinfo)
            dbsession.commit()

            dbfollowcompany = follow_company(employee_id = user.employee.id,company_id = dbcompanyinfo.id)
            dbsession.add(dbfollowcompany)

            dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id ).one()
            dbemployeefollow.company_count = dbemployeefollow.company_count+1
            dbsession.add(dbemployeefollow)

            #爬取文章
            url = 'http://spider.cd641dc781add4bc6b8ed119cee669cb7.cn-hangzhou.alicontainer.com/?keywords={short_name}'.format(short_name=short_name)
            req = urllib.request.Request(url)

            #公司和文章关联
            dbarticleinfo = dbsession.query(article.id).filter(article.text.like('%'+short_name+'%' )).all()
            companyarticle = []
            print(dbcompanyinfo.id)
            print(dbarticleinfo)
            for row in dbarticleinfo:
                dbcompanyarticleinfo = company_article(company_id = dbcompanyinfo.id ,article_id = row[0])
                companyarticle.append(dbcompanyarticleinfo)
            dbsession.add_all(companyarticle)
            dbsession.commit()

        else:
            dbfollowcompany = dbsession.query(follow_company).filter(follow_company.company_id == dbcompanyinfo.id,follow_company.employee_id == user.employee.id).one_or_none()
            if dbfollowcompany:
                #公司已经存在，且已取消关注数据
                if dbfollowcompany.is_follow == 0:
                    dbfollowcompany.is_follow = 1
                    dbfollowcompany.follow_time = datetime.now()
                    dbsession.add(dbcompanyinfo)

                    dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id ).one()
                    dbemployeefollow.company_count = dbemployeefollow.company_count+1
                    dbsession.add(dbemployeefollow)
            else: 
                #公司已经存在，无关注数据
                dbfollowcompany = follow_company(employee_id=user.employee.id,company_id=dbcompanyinfo.id)
                dbsession.add(dbfollowcompany)
                dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id ).one()
                dbemployeefollow.company_count = dbemployeefollow.company_count+1
                dbsession.add(dbemployeefollow)
        

        #操作员工关注文章
        faker_employee_article = []
        for row in dbsession.query(company_article.article_id).filter(company_article.company_id == dbcompanyinfo.id).all():
            dbemployeearticleinfo = dbsession.query(employee_article).filter(employee_article.article_id == row[0],employee_article.employee_id == user.employee.id).one_or_none()
            if dbemployeearticleinfo is None:
                dbemployeearticleinfo = employee_article(employee_id =user.employee.id,article_id = row[0],is_read = 0,is_invalid = 1,is_send=1,send_time = datetime.now())
                faker_employee_article.append(dbemployeearticleinfo)
        dbsession.add_all(faker_employee_article)
        dbsession.commit()
        dbsession.close()
        return None, 204, None