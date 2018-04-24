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
            for row in dbsession.query(industry.id,industry.industry_name,industry.children_count).join(follow_industry,industry.id==follow_industry.industry_id).filter(and_(follow_industry.employee_id==user.employee.id),follow_industry.is_follow==1).order_by(follow_industry.follow_time.desc()).all():
                industryinfodic = {}
                industryinfodic['id']=row[0]
                industryinfodic['industry_name'] = row[1]
                industryinfodic['children_count)'] = row[2]
                industryinfoarray.append(industryinfodic)
            respone['industry'] = industryinfoarray
        else:
            respone['industry'] = []
        dbsession.close()
        return respone, 200, None