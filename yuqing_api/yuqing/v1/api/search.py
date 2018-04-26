# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from core.PackageDB import company, industry, follow_company, follow_industry, _connectDBdata_
from sqlalchemy import and_


class Search(ApiHandler):

    def get(self):
        user = self.get_current_user()
        if not user.valid:
            return None, 401, None
        if user.session.employee_id is None:
            return None, 403, None
        key = self.args['key']
        follow_type = self.args['follow_type']
        searchtype = 0
        if 'type' in self.args:
            searchtype = self.args['type']
        dbsession = _connectDBdata_()
        infoarray = []
        if follow_type == 1:
            # 公司的信息
            dbcompanyinfo = dbsession.query(company.id, company.company_name, company.short_name)\
                .filter(company.company_name.like('%'+key+'%'))
            if searchtype > 0:
                dbcompanyinfo = dbcompanyinfo.join(follow_company, follow_company.company_id == company.id)\
                    .filter(follow_company.employee_id == user.employee.id, follow_company.is_follow == 1)
            dbcompanyinfo = dbcompanyinfo.all()
            dbsession.close()
            for row in dbcompanyinfo:
                infodic = {}
                infodic['id'] = row[0]
                infodic['company_name'] = row[1]
                infodic['short_name'] = row[2]
                infodic['follow_type'] = 1
                infoarray.append(infodic)
            respone = {'follows': infoarray}
            return respone, 200, None
        else:
            # 行业信息
            dbindustryinfo = dbsession.query(industry).filter(industry.industry_name.like('%'+key+'%'))
            if searchtype > 0:
                dbindustryinfo = dbindustryinfo.join(follow_industry, follow_industry.industry_id == industry.id)\
                    .filter(follow_industry.employee_id == user.employee.id, follow_industry.is_follow == 1)
            dbindustryinfo = dbindustryinfo.all()
            dbsession.close()
            for row in dbindustryinfo:
                infodic = {}
                infodic['id'] = row.id
                infodic['industry_name'] = row.industry_name
                infodic['children_count'] = row.children_count
                infodic['follow_type'] = 2

                children = []
                for childrenrow in [childrenmodel for childrenmodel in dbindustryinfo if childrenmodel.parent_id ==row.id]:
                    childrendic = {}
                    childrendic['id'] = childrenrow.id
                    childrendic['industry_name'] = childrenrow.industry_name
                    children.append(childrendic)
                infodic['children'] = children
                infoarray.append(infodic)
            respone = {'follows': infoarray}
            return respone, 200, None