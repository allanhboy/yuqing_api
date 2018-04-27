# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from sqlalchemy import and_,exists
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
        
        datenow = datetime.now()
        dbsession = _connectDBdata_()
        try:
            #关注公司信息
            if follow_type == 1:
                dbcompanyinfo = dbsession.query(follow_company).filter(and_(follow_company.employee_id == user.employee.id),follow_company.company_id == id).one_or_none()
                #对已取消进行关注操作
                if dbcompanyinfo:
                    if dbcompanyinfo.is_follow == 1:
                        return None, 204, None
                    dbcompanyinfo.is_follow = 1
                    dbcompanyinfo.follow_time = datenow
                #第一次关注 
                else: 
                
                    dbcompanyinfo = follow_company(employee_id=user.employee.id,company_id= id)
                    dbsession.add(dbcompanyinfo)
                dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id).update({'company_count':employee_follow.company_count+1})

                #员工关注文章
                faker_employee_article = []
                for row in dbsession.query(company_article.article_id,article.publish_time)\
                    .join(article,article.id == company_article.article_id)\
                    .filter(company_article.company_id == dbcompanyinfo.company_id)\
                .filter(~exists().where(employee_article.article_id == company_article.article_id).where(employee_article.employee_id == user.employee.id)).all():
                    dbemployeearticleinfo = employee_article(employee_id =user.employee.id,article_id = row[0],is_read = 0,is_invalid = 0,is_send=1,send_time = datenow)
                    if row[1].strftime('%Y/%m/%d') < datenow.strftime('%Y/%m/%d'):
                        dbemployeearticleinfo.is_read =1
                    faker_employee_article.append(dbemployeearticleinfo)
                dbsession.add_all(faker_employee_article)
            #关注行业信息
            if follow_type == 2:
                
                for row in dbsession.execute('select id from industry where FIND_IN_SET(id,getChildrenOrg({id}))'.format(id=id)).fetchall():
                    dbindustryinfo = dbsession.query(follow_industry).filter(and_(follow_industry.employee_id == user.employee.id,follow_industry.industry_id == row[0])).one_or_none()
                    #对已取消进行关注操作
                    if dbindustryinfo:
                        if dbindustryinfo.is_follow == 0:
                            dbindustryinfo.is_follow = 1
                            dbindustryinfo.follow_time = datenow
                            dbsession.add(dbindustryinfo)
                        else:
                            continue
                    else:
                    #第一次关注 
                        dbindustryinfo = follow_industry(employee_id=user.employee.id,industry_id= row[0])
                        dbsession.add(dbindustryinfo)
                    dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id).update({'industry_count':employee_follow.industry_count+1})


                #员工关注文章
                faker_employee_article = []
                for row in dbsession.query(industry_article.article_id,article.publish_time)\
                    .join(article,article.id == industry_article.article_id)\
                    .filter(industry_article.industry_id == dbindustryinfo.industry_id)\
                .filter(~exists().where(employee_article.article_id == industry_article.article_id).where(employee_article.employee_id == user.employee.id)).all():
                    dbemployeearticleinfo = employee_article(employee_id =user.employee.id,article_id = row[0],is_read = 0,is_invalid = 0,is_send=1,send_time = datenow)
                    if row[1].strftime('%Y/%m/%d') < datenow.strftime('%Y/%m/%d'):
                        dbemployeearticleinfo.is_read = 1
                    faker_employee_article.append(dbemployeearticleinfo)
                dbsession.add_all(faker_employee_article)
            dbsession.commit()
            dbsession.close()
            return None, 204, None
        except:
            return None, 400, None
        finally:
            dbsession.close() 

    def delete(self):
        user = self.get_current_user()
        if not user.valid:
            return None ,401,None
        if user.employee.id is None:
            return None ,403,None
        
        follow_type = self.json['follow_type']
        id = self.json['id']

        datenow = datetime.now()
        dbsession = _connectDBdata_()

        try:
        #取消关注公司信息
            if follow_type == 1:
                dbcompanyinfo = dbsession.query(follow_company).filter(and_(follow_company.employee_id == user.employee.id),follow_company.company_id == id).one_or_none()  
                if dbcompanyinfo is not None:  
                    dbcompanyinfo.is_follow = 0
                    dbcompanyinfo.unfollow_time = datenow
                    dbsession.add(dbcompanyinfo)
                    dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id,employee_follow.industry_count-1>=0).update({'company_count':employee_follow.company_count-1})
            #取消关注行业信息
            if follow_type == 2:
                for row in dbsession.execute('select id from industry where FIND_IN_SET(id,getChildrenOrg({id}))'.format(id=id)).fetchall():
                    dbindustryinfo = dbsession.query(follow_industry).filter(and_(follow_industry.employee_id == user.employee.id,follow_industry.industry_id == row[0]),follow_industry.is_follow==1).one_or_none()
                    if dbindustryinfo is not None:
                        dbindustryinfo.is_follow = 0
                        dbindustryinfo.unfollow_time = datenow
                        dbsession.add(dbindustryinfo)
                        dbsession.query(employee_follow).filter(and_(employee_follow.id == user.employee.id),employee_follow.industry_count-1>=0).update({'industry_count':employee_follow.industry_count-1})
            dbsession.commit()
            return None, 204, None
        except:
            return None, 400, None
        finally:
            dbsession.close() 