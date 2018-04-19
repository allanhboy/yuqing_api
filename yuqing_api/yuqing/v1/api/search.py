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
            dbinfo = dbsession.query(company.id,company.company_name,company.short_name).filter(company.company_name.like('%'+key+'%' )).all()
            while i< (len(dbinfo)):
                infodic ={}
                infodic['id']=dbinfo[i][0]
                infodic['company_name'] = dbinfo[i][1]
                infodic['short_name)'] = dbinfo[i][2]
                infodic['follow_type']=1
                infoarray.append(infodic)
                i=i+1
            respone={'follows':infoarray}
            return respone, 200, None
        else:
            dbinfo = dbsession.query(industry.id,industry.industry_name,industry.children_count).filter(industry.industry_name.like('%'+key+'%' )).all()
            while i< (len(dbinfo)):
                infodic ={}
                infodic['id']=dbinfo[i][0]
                infodic['industry_name'] = dbinfo[i][1]
                infodic['children_count)'] = dbinfo[i][2]
                infodic['follow_type']=2
                infoarray.append(infodic)
                i=i+1
            respone={'follows':infoarray}
            return respone, 200, None