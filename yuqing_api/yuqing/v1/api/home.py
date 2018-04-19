# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from core import PackageDB,PackageSession

class Home(ApiHandler):

    def get(self):             
        user = self.get_current_user()
        if user.valid:
            user.employee
        
            return {}, 200, None