# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


from sqlalchemy import and_
from datetime import datetime, timedelta
from core.PackageDB import follow_company,follow_industry,employee_follow,_connectDBdata_

class Follow(ApiHandler):

    def post(self):
        follow_type = self.json['follow_type']
        id = self.json['id']
        user = self.get_current_user()
        if user.valid:
            dbsession = _connectDBdata_()
            if follow_type == 1:
                dbcompanyinfo = dbsession.query(follow_company).filter(and_(follow_company.employee_id == user.employee.id),follow_company.company_id == id).one_or_none()
                if dbcompanyinfo:
                    dbcompanyinfo.is_follow = 1
                    dbcompanyinfo.follow_time = datetime.now()
                    dbsession.add(dbcompanyinfo)
                else:     
                    dbcompanyinfo = follow_company(employee_id=user.employee.id,company_id= id)
                    dbsession.add(dbcompanyinfo)
                dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id).one_or_none()
                dbemployeefollow.company_count = dbemployeefollow.company_count+1
                dbsession.add(dbemployeefollow)
                dbsession.commit()
            if follow_type == 2:
                dbindustryinfo = dbsession.query(follow_industry).filter(and_(follow_industry.employee_id == user.employee.id,follow_industry.industry_id == id)).one_or_none()
                if dbindustryinfo:
                    dbindustryinfo.is_follow = 1
                    dbindustryinfo.follow_time = datetime.now()
                    dbsession.add(dbindustryinfo)
                else:     
                    dbindustryinfo = follow_company(employee_id=user.employee.id,industry_id= id)
                    dbsession.add(dbindustryinfo)
                dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id).one_or_none()
                dbemployeefollow.industry_count = dbemployeefollow.instury_count+1
                dbsession.add(dbemployeefollow)
                dbsession.commit()
        return None, 204, None

    def delete(self):
        follow_type = self.json['follow_type']
        id = self.json['id']
        user = self.get_current_user()
        if user.valid:
            dbsession = _connectDBdata_()
            if follow_type == 1:
                dbcompanyinfo = dbsession.query(follow_company).filter(and_(follow_company.employee_id == user.employee.id),follow_company.company_id == id).one_or_none()      
                dbcompanyinfo.is_follow = 0
                dbcompanyinfo.unfollow_time = datetime.now()
                dbsession.add(dbcompanyinfo)
                dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id).one_or_none()
                dbemployeefollow.company_count = dbemployeefollow.company_count-1
                dbsession.add(dbemployeefollow)
                dbsession.commit()
            if follow_type == 2:
                dbindustryinfo = dbsession.query(follow_industry).filter(and_(follow_industry.employee_id == user.employee.id,follow_industry.industry_id == id)).one_or_none()
                dbindustryinfo.is_follow = 0
                dbindustryinfo.unfollow_time = datetime.now()
                dbsession.add(dbindustryinfo)
                dbemployeefollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id).one_or_none()
                dbemployeefollow.industry_count = dbemployeefollow.instury_count-1
                dbsession.add(dbemployeefollow)
                dbsession.commit()
        return None, 204, None