# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from sqlalchemy import and_

from core.PackageDB import (_connectDBdata_, company, follow_company,
                            follow_industry, industry)

from . import ApiHandler
from .. import schemas


class Search(ApiHandler):

    def get(self):
        user = self.get_current_user()
        if not user.valid:
            return None, 401, None
        if user.session.employee_id is None:
            return None, 403, None
        key = self.args['key']
        if key is None or len(key) <= 0:
            return None, 404, None
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
        else:
            # 行业信息
            dbindustryinfo = dbsession.query(industry)#.filter(industry.industry_name.like('%'+key+'%'))
            if searchtype > 0:
                dbindustryinfo = dbindustryinfo.join(follow_industry, follow_industry.industry_id == industry.id)\
                    .filter(follow_industry.employee_id == user.employee.id, follow_industry.is_follow == 1)
            dbindustryinfo = dbindustryinfo.all()
            dbsession.close()
            for row in [t1 for t1 in dbindustryinfo if key in t1.industry_name]:
                children=[(t1) for t1 in dbindustryinfo if t1.parent_id ==row.id]
                infodic = {}
                infodic['id'] = row.id
                infodic['industry_name'] = row.industry_name
                infodic['children_count'] = len(children)
                infodic['follow_type'] = 2

                _children = []
                for childrenrow in [(t1) for t1 in dbindustryinfo if t1.parent_id ==row.id]:
                    childrendic = {}
                    childrendic['id'] = childrenrow.id
                    childrendic['industry_name'] = childrenrow.industry_name
                    children.append(childrendic)
                infodic['children'] = _children
                infoarray.append(infodic)
        respone = {'follows': infoarray}
        return respone, 200, None
