# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from core.PackageDB import company,industry,follow_company,follow_industry,_connectDBdata_
from sqlalchemy import and_

class Search(ApiHandler):

    def get(self):      
        user = self.get_current_user()
        if not user.valid:
            return None ,401,None
        if user.session.employee_id is None:
            return None ,403,None
        key = self.args['key']
        follow_type = self.args['follow_type']
        searchtype = 0
        if 'type' in self.args:
            searchtype = self.args['type']
        dbsession =_connectDBdata_()
        infoarray =[]
        if follow_type == 1:
            #公司的信息
            dbcompanyinfo=dbsession.query(company.id,company.company_name,company.short_name)\
                .filter(company.company_name.like('%'+key+'%' ))
            if searchtype > 0:
                dbcompanyinfo=dbcompanyinfo.join(follow_company,follow_company.company_id == company.id)
                dbcompanyinfo=dbcompanyinfo.filter(follow_company.employee_id == user.employee.id)              
            dbcompanyinfo=dbcompanyinfo.all()
            for row in dbcompanyinfo:
                infodic ={}
                infodic['id']=row[0]
                infodic['company_name'] = row[1]
                infodic['short_name'] = row[2]
                infodic['follow_type']=1
                infoarray.append(infodic)
            respone={'follows':infoarray}
            dbsession.close()
            return respone, 200, None
        else:
            #行业信息
            dbindustryinfo=dbsession.query(industry.id,industry.industry_name,industry.children_count)\
                .filter(industry.industry_name.like('%'+key+'%' ))
            if searchtype > 0:
                dbindustryinfo=dbindustryinfo.join(follow_industry,follow_industry.industry_id == industry.id)
                dbindustryinfo=dbindustryinfo.filter(follow_industry.employee_id == user.employee.id)              
            dbindustryinfo=dbindustryinfo.all()
            for row in dbindustryinfo:
                infodic ={}
                infodic['id']=row[0]
                infodic['industry_name'] =row[1]
                infodic['children_count'] = row[2]
                infodic['follow_type']=2
                children = []
                #子行业信息
                for  childrenrow in dbsession.query(industry.id,industry.industry_name).filter(industry.parent_id == row[0]).all():
                    childrendic = {}
                    childrendic['id'] = childrenrow[0]
                    childrendic['industry_name'] = childrenrow[1]
                    children.append(childrendic)
                infodic['children'] = children
                infoarray.append(infodic)
            respone={'follows':infoarray}
            dbsession.close()
            return respone, 200, None