# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from sqlalchemy import and_
from core.PackageDB import follow_company,follow_industry,company,employee_follow,industry,_connectDBdata_
import json

class Follows(ApiHandler):

    def get(self):
        user = self.get_current_user()
        if not user.valid:
            return None ,401,None
        if user.session.employee_id is None:
            return None ,403,None

        dbsession = _connectDBdata_()
        dbfollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id).one()
        respone = {}
        #公司关注信息
        if dbfollow.company_count > 0:
            companyinfoarray = []
            for row in dbsession.query(company.id,company.company_name,company.short_name).join(follow_company,company.id==follow_company.company_id).filter(and_(follow_company.employee_id==user.employee.id),follow_company.is_follow==1).order_by(follow_company.follow_time.desc()).all():
                companyinfodic = {}
                companyinfodic['id']=row[0]
                companyinfodic['company_name'] = row[1]
                companyinfodic['short_name'] = row[2]
                companyinfoarray.append(companyinfodic)
            respone['company'] = companyinfoarray
        else:
            respone['company'] = []
        #行业关注信息
        if dbfollow.industry_count >0:
            industryinfoarray = []
            db = dbsession.query(industry).join(follow_industry,industry.id==follow_industry.industry_id).filter(and_(follow_industry.employee_id==user.employee.id),follow_industry.is_follow==1).order_by(follow_industry.follow_time.desc()).all()
            for row in db:
                if row.parent_id is not None:
                    parents=[(t1) for t1 in db if t1.id ==row.parent_id]
                    print(row.id)
                    print(row.parent_id)
                    print(parents)
                    print('--------------')
                    print(parents)
                    if len(parents)>0:
                        continue
                industryinfodic = {}
                industryinfodic['id']=row.id
                industryinfodic['industry_name'] = row.industry_name
                industryinfodic['children_count'] = row.children_count
                industryinfodic['children_industry'] = factorial(row.id,db)
                industryinfoarray.append(industryinfodic)
            respone['industry'] = industryinfoarray
        else:
            respone['industry'] = []
        return respone, 200, None

def factorial(parent_id,db):
    fatherindustry = []
    curectchilddb=[(t1) for t1 in db if t1.parent_id ==parent_id]
    for curectchilddbrow in curectchilddb:
        childrendic = {}
        childrendic['id'] = curectchilddbrow.id
        childrendic['industry_name'] = curectchilddbrow.industry_name
        childrendic['children_count'] = curectchilddbrow.children_count
        childrendic['children_industry']=factorial(curectchilddbrow.id,db)
        fatherindustry.append(childrendic)
    return fatherindustry