# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from sqlalchemy import and_
from datetime import datetime,timedelta
from core.PackageDB import follow_company,follow_industry,employee_follow,company_article,industry_article,employee_article,article,_connectDBdata_

class Follow(ApiHandler):

    def post(self):
        user = self.get_current_user()
        if not user.valid:
            return None ,401,None
        if user.session.employee_id is None:
            return None ,403,None
        follow_type = self.json['follow_type']
        id = self.json['id']

        dbsession = _connectDBdata_()
        #关注公司信息
        if follow_type == 1:
            dbcompanyinfo = dbsession.query(follow_company).filter(and_(follow_company.employee_id == user.employee.id),follow_company.company_id == id).one_or_none()
            #对已取消进行关注操作
            if dbcompanyinfo:
                if dbcompanyinfo.is_follow == 1:
                     return None, 204, None
                dbcompanyinfo.is_follow = 1
                dbcompanyinfo.follow_time = datetime.now()
                dbsession.add(dbcompanyinfo)
            else: 
            #第一次关注    
                dbcompanyinfo = follow_company(employee_id=user.employee.id,company_id= id)
                dbsession.add(dbcompanyinfo)
            dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id).one_or_none()
            dbemployeefollow.company_count = dbemployeefollow.company_count+1
            dbsession.add(dbemployeefollow)

            #员工关注文章
            faker_employee_article = []
            for row in dbsession.query(company_article.article_id,article.publish_time).join(article,article.id == company_article.article_id).filter(company_article.company_id == dbcompanyinfo.company_id).all():
                dbemployeearticleinfo = dbsession.query(employee_article).filter(and_(employee_article.article_id == row[0],employee_article.employee_id == user.employee.id)).one_or_none()
                if dbemployeearticleinfo is None:
                    if row[1].strftime('%Y/%m/%d')>=datetime.now().strftime('%Y/%m/%d'):
                        dbemployeearticleinfo = employee_article(employee_id =user.employee.id,article_id = row[0],is_read = 0,is_invalid = 0,is_send=1,send_time = datetime.now())
                    else:
                        dbemployeearticleinfo = employee_article(employee_id =user.employee.id,article_id = row[0],is_read = 1,is_invalid = 0,is_send=1,send_time = datetime.now())
                    faker_employee_article.append(dbemployeearticleinfo)
            dbsession.add_all(faker_employee_article)
            dbsession.commit()
        #关注行业信息
        if follow_type == 2:
            dbindustryinfo = dbsession.query(follow_industry).filter(and_(follow_industry.employee_id == user.employee.id,follow_industry.industry_id == id)).one_or_none()
            #对已取消进行关注操作
            if dbindustryinfo:
                if dbindustryinfo.is_follow == 1:
                    return None, 204, None
                dbindustryinfo.is_follow = 1
                dbindustryinfo.follow_time = datetime.now()
                dbsession.add(dbindustryinfo)
            else:
            #第一次关注    
                dbindustryinfo = follow_industry(employee_id=user.employee.id,industry_id= id)
                dbsession.add(dbindustryinfo)
            dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id).one_or_none()
            dbemployeefollow.industry_count = dbemployeefollow.industry_count+1
            dbsession.add(dbemployeefollow)

            #员工关注文章
            faker_employee_article = []
            for row in dbsession.query(industry_article.article_id,article.publish_time).join(article,article.id == industry_article.article_id).filter(industry_article.industry_id == dbindustryinfo.industry_id).all():
                dbemployeearticleinfo = dbsession.query(employee_article).filter(and_(employee_article.article_id == row[0],employee_article.employee_id == user.employee.id)).one_or_none()
                if dbemployeearticleinfo is None:
                    if row[1].strftime('%Y/%m/%d')>=datetime.now().strftime('%Y/%m/%d'):
                        dbemployeearticleinfo = employee_article(employee_id =user.employee.id,article_id = row[0],is_read = 0,is_invalid = 0,is_send=1,send_time = datetime.now())
                    else:
                        dbemployeearticleinfo = employee_article(employee_id =user.employee.id,article_id = row[0],is_read = 1,is_invalid = 0,is_send=1,send_time = datetime.now())
                    faker_employee_article.append(dbemployeearticleinfo)
            dbsession.add_all(faker_employee_article)

            dbsession.commit()
        dbsession.close()
        return None, 204, None

    def delete(self):
        user = self.get_current_user()
        if not user.valid:
            return None ,401,None
        if user.employee.id is None:
            return None ,403,None
        follow_type = self.json['follow_type']
        id = self.json['id']

        dbsession = _connectDBdata_()
        #取消关注公司信息
        if follow_type == 1:
            dbcompanyinfo = dbsession.query(follow_company).filter(and_(follow_company.employee_id == user.employee.id),follow_company.company_id == id).one_or_none()      
            dbcompanyinfo.is_follow = 0
            dbcompanyinfo.unfollow_time = datetime.now()
            dbsession.add(dbcompanyinfo)
            dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id).one_or_none()
            dbemployeefollow.company_count = dbemployeefollow.company_count-1
            dbsession.add(dbemployeefollow)
            dbsession.commit()
        #取消关注行业信息
        if follow_type == 2:
            dbindustryinfo = dbsession.query(follow_industry).filter(and_(follow_industry.employee_id == user.employee.id,follow_industry.industry_id == id)).one_or_none()
            dbindustryinfo.is_follow = 0
            dbindustryinfo.unfollow_time = datetime.now()
            dbsession.add(dbindustryinfo)
            dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id).one_or_none()
            dbemployeefollow.industry_count = dbemployeefollow.industry_count-1
            dbsession.add(dbemployeefollow)
            dbsession.commit()
        dbsession.close()
        return None, 204, None