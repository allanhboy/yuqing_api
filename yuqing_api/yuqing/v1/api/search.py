# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from core.PackageDB import company,industry,_connectDBdata_

class Search(ApiHandler):

    def get(self):
        key = self.args['key']
        follow_type = self.args['follow_type']
        dbsession =_connectDBdata_()
        i=0
        infoarray =[]
        if follow_type == 1:
            #公司的信息
            for row in dbsession.query(company.id,company.company_name,company.short_name).filter(company.company_name.like('%'+key+'%' )).all():
                infodic ={}
                infodic['id']=row[0]
                infodic['company_name'] = row[1]
                infodic['short_name)'] = row[2]
                infodic['follow_type']=1
                infoarray.append(infodic)
            respone={'follows':infoarray}
            return respone, 200, None
        else:
            #行业信息
            for row in dbsession.query(industry.id,industry.industry_name,industry.children_count).filter(industry.industry_name.like('%'+key+'%' )).all():
                infodic ={}
                infodic['id']=row[0]
                infodic['industry_name'] =row[1]
                infodic['children_count)'] = row[2]
                infodic['follow_type']=2
                children = []
                @#子行业信息
                for  childrenrow in dbsession.query(industry.id,industry.industry_name).filter(industry.parent_id == row[0]).all():
                    childrendic = {}
                    childrendic['id'] = childrenrow[0]
                    childrendic['industry_name'] = childrenrow[0]
                    children.append(childrendic)
                infodic['children'] = children
                infoarray.append(infodic)
            respone={'follows':infoarray}
            return respone, 200, None