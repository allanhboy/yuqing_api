# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from core.PackageDB import _connectDBdata_, employee_follow

from . import ApiHandler
from .. import schemas


class FollowState(ApiHandler):
    def get(self):
        user = self.get_current_user()
        if not user.valid:
            return None, 401, None
        if user.session.employee_id is None:
            return None, 403, None
        dbsession = _connectDBdata_()
        dbemployeefollow = dbsession.query(employee_follow).filter(
            employee_follow.id == user.employee.id).one_or_none()
        dbsession.close()
        if dbemployeefollow is not None:
            response = {
                'company': dbemployeefollow.company_count,
                'industry': dbemployeefollow.industry_count
            }
            return response, 200, None
        return None, 200, None
