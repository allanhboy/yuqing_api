# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


from core.PackageDB import follow_company,follow_industry,company,employee_follow,industry,_connectDBdata_
import json

class Follows(ApiHandler):

    def get(self):
        user = self.get_current_user()
        if user.valid:
            dbsession = _connectDBdata_()
            dbfollow = dbsession.query(employee_follow).filter(employee_follow.id == user.employee.id).one()
            respone = {}
            if dbfollow.company_count > 0:
                dbcompanyinfo = dbsession.query(company.id,company.company_name,company.short_name,follow_company.is_follow).join(follow_company,company.id==follow_company.company_id).filter(follow_company.employee_id==user.employee.id).all()
                i=0
                companyinfoarray = []
                while i< (len(dbcompanyinfo)):
                    if dbcompanyinfo[i][3]:
                        companyinfodic = {}
                        companyinfodic['id']=dbcompanyinfo[i][0]
                        companyinfodic['company_name'] = dbcompanyinfo[i][1]
                        companyinfodic['short_name'] = dbcompanyinfo[i][2]
                        companyinfoarray.append(companyinfodic)
                    i=i+1
                respone['company'] = companyinfoarray
            if dbfollow.industry_count >0:
                dbindustryinfo = dbsession.query(industry.id,industry.industry_name,industry.children_count,follow_industry.is_follow).join(follow_industry,industry.id==follow_industry.industry_id).filter(follow_industry.employee_id==user.employee.id).all()
                i=0
                industryinfoarray = []
                while i< (len(dbindustryinfo)):
                    if dbindustryinfo[i][3]:
                        industryinfodic = {}
                        industryinfodic['id']=dbindustryinfo[i][0]
                        industryinfodic['industry_name'] = dbindustryinfo[i][1]
                        industryinfodic['children_count)'] = dbindustryinfo[i][2]
                        industryinfoarray.append(industryinfodic)
                    i=i+1
                respone['industry'] = industryinfoarray
        return respone, 200, None