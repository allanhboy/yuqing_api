# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


from datetime import datetime, timedelta

from core.PackageDB import company,employee_follow,follow_company,_connectDBdata_

class Newfollow(ApiHandler):

    def post(self):
        company_name = self.json['company_name']
        short_name = self.json['short_name']
        user = self.get_current_user()
        if user.valid:
            dbsession =_connectDBdata_()
            dbcompanyinfo = dbsession.query(company).filter(company.company_name == company_name).one_or_none()
            #添加新的公司
            if dbcompanyinfo is None:
                dbcompanyinfo = company(company_name = company_name,short_name = short_name,is_chinaipo = 0,url = '')
                dbsession.add(dbcompanyinfo)
                dbsession.commit()
                
                print(dbcompanyinfo.id)
                dbfollowcompany = follow_company(employee_id = user.employee.id,company_id = dbcompanyinfo.id)
                dbsession.add(dbfollowcompany)
                dbsession.commit()

                dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id ).one()
                dbemployeefollow.company_count = dbemployeefollow.company_count+1
                dbsession.add(dbemployeefollow)
                dbsession.commit()
            else:
                dbfollowcompany = dbsession.query(follow_company).filter(follow_company.company_id == dbcompanyinfo.id).one_or_none()
                if dbfollowcompany:
                    #公司已经存在，且有关注数据
                    print(dbfollowcompany.is_follow)
                    #公司已经存在，且已取消关注数据
                    if dbfollowcompany.is_follow == 0:
                        dbfollowcompany.is_follow = 1
                        dbfollowcompany.follow_time = datetime.now()
                        dbsession.add(dbcompanyinfo)

                        dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id ).one()
                        dbemployeefollow.company_count = dbemployeefollow.company_count+1
                        dbsession.add(dbemployeefollow)
                        dbsession.commit()
                else: 
                    #公司已经存在，无关注数据
                    dbfollowcompany = follow_company(employee_id=user.employee.id,company_id=dbcompanyinfo.id)
                    dbsession.add(dbfollowcompany)
                    dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id ).one()
                    dbemployeefollow.company_count = dbemployeefollow.company_count+1
                    dbsession.add(dbemployeefollow)
                    dbsession.commit()
            return None, 204, None
        else:
            return None ,400,None